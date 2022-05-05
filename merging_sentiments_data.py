import pandas as pd

#Merging csvs and exporting a combined file for creating a multiple bar chart
transcripts_df = pd.read_csv('transcript_sentiments.csv')
title_df = pd.read_csv('title_sentiments.csv')
description_df = pd.read_csv('description_sentiments.csv')
tandd_df = pd.read_csv('roundone.csv')

allsentiments_df=pd.merge(tandd_df, transcripts_df, on="url", how="outer", indicator="true")
allsentiments_df.to_csv("master_all_sentiments.csv", index=False, encoding='UTF8')










