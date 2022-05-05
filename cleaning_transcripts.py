from matplotlib.pyplot import axis
import pandas as pd
import re

ted_df = pd.read_csv('location/ted_inner.csv')

#removing brackets, "" and special characters
ted_df["ntranscript"] = ted_df["transcript"].map(lambda x: re.sub("\(.*?\)", " ", x))
ted_df = ted_df.drop("transcript", axis=1)

ted_df.to_csv("location/ted_inner2.csv")