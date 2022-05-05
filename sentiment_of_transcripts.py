from google.cloud import language
import pandas

#wrapper around Google Cloud Sentiment Analysis
def analyze_text_sentiment(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document=document)

    sentiment = response.document_sentiment
    results = {
        'text':text,
        'score':sentiment.score,
        'magnitude': sentiment.magnitude
    }

    return results

sentiments_df = pandas.read_csv("location/ted_inner2.csv")
len_sentiments = len(sentiments_df)

#sending the cleaned column 'transcript' for sentiment analysis
for idx,row in sentiments_df.iterrows():
    print(idx, "of", len_sentiments)
    response = analyze_text_sentiment(row["ntranscript"])
    sentiments_df.loc[idx, "score"] = response["score"]
    sentiments_df.loc[idx, "magnitude"] = response["magnitude"]

#saving the output locally
sentiments_df.to_csv("location/transcript_sentiments.csv")
