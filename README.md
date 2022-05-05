# pfch_finalproject2022
Analyzing ted talks using python

This repository contains the final project files created while studying Programming for Cultural Heritage (INFO 664-01) at Pratt Institute. The project was completed in the Spring 2022 semester. Ted talks data was collected from Kaggle. There were two datasets available on the link (https://www.kaggle.com/datasets/rounakbanik/ted-talks). The file “main.csv” dataset contains information about all talks including number of views, number of comments, descriptions, speakers and titles. The transcripts dataset contains the transcripts for all talks available on ted.com. Both the datasets have information on 2553 talks from the first video uploaded on ted.com in 2006 to Sep, 2017.

This project is centered around sentiment analysis of the dataset. My interest in analyzing qualitative data motivated me to work towards this topic. Sentiment analysis was done following a sample code on the Google Cloud Natural Language’s website. The process of doing sentiment analysis using Google Cloud begins by installing google cloud library on the system, for which one first needs to get a unique API key to install the library in the environment. Once installed, the next step is to import the ‘language’ package from ‘google.cloud’ which then uses ‘def analyze_text_sentiment(text)’ to analyze text and return results for ‘text,’ ‘score’ and ‘magnitude.’ ‘Text’ is the portion of the ted talks content being analyzed, ‘score’ is the analysis of the sentiment (if the emotion is negative, positive or neutral or -1, 1 or 0), and ‘magnitude’ is the intensity of the emotion. Magnitude can be any number above 0. 

After conducting sentiment analysis, the project used multiple python libraries and packages to analyze the dataset. For example, wordcloud is used to create transcript and title word clouds, beautiful soup to extract speaker details from Wikipedia and matplotlib to visualize charts. Below is the sequence in which the repository files were created - 

merging_source_ted_files.py: The two datasets were joined using the url column. 

cleaning_transcripts.py: The merged files’ transcript column is cleaned for sentiment analysis

sentiments_of_descriptions.py, sentiments_of_titles.py, sentiments_of_transcripts.py: The cleaned file was then sent to Google Cloud Natural Language API for sentiment analysis. 

wordclouds.py: Wordclouds of the top 20 and bottom 20 viewed videos’ transcript and titles are created

merging_sentiments_data.py: The transcript, title and description scores and magnitudes are merged to create one dataset for visualizations

sentiment_visuals.py: Various visualizations are created using the sentiment scores and magnitudes

sentiments_overview_visualizations.py: Overview of sentiments data is created using this file

split_tags.py: Calculating the number of views every tag has received

extracting_wikipedia_data.py: Using wikipedia API to extract author nationality details

extracting_transcript_sentences.py: Extract transcript sentiments per minute for the top 5 and bottom 5 videos sorted on the basis of likes

merging_files_ted.py: To merge uncleaned transcripts with the main dataset for analyzing audience reaction

funny_element_count.py: Finding out the most funny and the least funny videos, and trying correlation between funniness and views

regression.py: Attempted answering the question - Can we predict video views if we know the length of a video and number of laughs per minute? 

An analysis report was submitted alongside this repository.
