import pandas as pd
teddf = pd.read_csv("location/transcript_sentiments.csv")
teddf = teddf.dropna()
teddf.reset_index(drop=True, inplace=True)
print(1)

teddf["funny_count"] = 0
for idx, row in teddf.iterrows():
    teddf["funny_count"].iloc[idx] = row["ntranscript"].count('(Laughter)')

teddf["duration_minutes"] = (teddf["duration"]/60).round(decimals=1)
teddf["nfunny_count"] = (teddf["funny_count"]/teddf["duration_minutes"]).round(decimals=1)
teddf = teddf.sort_values("nfunny_count")
print(2)
download_date = 1514782799
teddf['age'] = (download_date - teddf["published_date"])/(1651291081 - 1619755081)
teddf["age"] = teddf["age"].round(decimals=2)
teddf = teddf.sort_values("age")
teddf["nviews"] = teddf["views"]/teddf["age"]
teddf["ncomments"] = teddf["comments"]/teddf["age"]
teddf = teddf.sort_values(["nviews"])

from sklearn import linear_model
from sklearn import preprocessing

print(3)
model = linear_model.LinearRegression(fit_intercept=False)

inputdata = teddf[["ncomments"]]
data_normalized = preprocessing.normalize(inputdata,norm='l2')

#adding multiple combinations of variables here to see which regression models work
model.fit(data_normalized,  teddf[["nviews"]])
print("Coefficients: \n", model.coef_, model.score(data_normalized, teddf[["nviews"]]))
