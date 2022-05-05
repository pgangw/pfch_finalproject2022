# import csv
from collections import OrderedDict
import pandas as pd

#Merging csvs and exporting a combined file
ted_main_df = pd.read_csv('location/ted_main.csv')
ted_transcripts_df = pd.read_csv('location/transcripts.csv')

ted_df=pd.merge(ted_main_df, ted_transcripts_df, on="url", indicator="true")
ted_df.to_csv("location/ted_inner.csv", index=False, encoding='UTF8')












