import pandas as pd

teddf = pd.read_csv("location/ted.csv")
teddf = teddf.dropna()
teddf.reset_index(drop=True, inplace=True)

teddf["funny_count"] = 0
for idx, row in teddf.iterrows():
    teddf["funny_count"].iloc[idx] = row["transcript"].count('(Laughter)')

teddf["duration_minutes"] = (teddf["duration"]/60).round(decimals=1)

#dividing funny count by duration to nornalize the data 
teddf["nfunny_count"] = (teddf["funny_count"]/teddf["duration_minutes"]).round(decimals=1)
teddf = teddf.sort_values("nfunny_count")

#assuming all videos were posted by Dec 2017
download_date = 1514782799
teddf['age'] = (download_date - teddf["published_date"])/(1651291081 - 1619755081)
teddf["age"] = teddf["age"].round(decimals=2)
teddf = teddf.sort_values("age")
teddf["nviews"] = teddf["views"]/teddf["age"]
teddf["ncomments"] = teddf["comments"]/teddf["age"]
teddf = teddf.sort_values(["nviews"])

#correlating funny count and normalized views
funny_views_corr = teddf['nfunny_count'].corr(teddf['nviews'])
funny_comments_corr = teddf['nfunny_count'].corr(teddf['ncomments'])

#Adding nviews to ("minutewise_sentiment.csv")
basedf = pd.read_csv("minutewise_sentiment.csv")
basedf = basedf.merge(teddf, 'left', "url")
basedf.to_csv("nviews_sentiments.csv")
print(basedf.columns)