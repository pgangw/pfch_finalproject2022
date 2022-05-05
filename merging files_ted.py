import pandas as pd
import nltk
nltk.download()

#Merging csvs and exporting a combined file
ted_main_df = pd.read_csv('ted_main.csv')
ted_transcripts_df = pd.read_csv('tedtranscripts.csv')

ted_df=pd.merge(ted_main_df, ted_transcripts_df, on="url", how="outer", indicator="true")
ted_df.to_csv("ted.csv", index=False, encoding='UTF8')










