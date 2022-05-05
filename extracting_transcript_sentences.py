import pandas as pd
from google.cloud import language
import stanza

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

from itertools import islice
def chunk(it, size):
    it = iter(it)
    while slice := tuple(islice(it, size)):
        yield slice


talks = []

download_date = 1514782799

transcript_df = pd.read_csv("transcript_sentiments.csv")

#taking videos with views over 1M
Mtranscript_df = transcript_df[transcript_df["views"] >= 1000000]

#Normalizing the data by counting the number of years it has been online. The dates in the dataset are in timestamp format.
Mtranscript_df['age'] = (download_date - Mtranscript_df["published_date"])/(1651291081 - 1619755081)
Mtranscript_df["age"] = Mtranscript_df["age"].round(decimals=2)
Mtranscript_df = Mtranscript_df.sort_values("age")
Mtranscript_df["nviews"] = Mtranscript_df["views"]/Mtranscript_df["age"]
Mtranscript_df = Mtranscript_df.sort_values(["nviews"])

topbot5 = Mtranscript_df.iloc[:5,:].append(Mtranscript_df.iloc[-5:,:])

#storing the text by title
transcript_lookup = dict(zip(topbot5["title"], topbot5["ntranscript"]))

nlp = stanza.Pipeline(lang='en', processors='tokenize')
sentimentsdf = pd.DataFrame(columns = ["title", "url","transcript", "minute", "score", "magnitude"])

for idx, talk in topbot5.iterrows():
    print(talk['title'])
    print("length:",talk['duration'])
    doc = nlp(talk['ntranscript'])

    sentences = []
    for sentence in doc.sentences:
        sentences.append(sentence.text)

	#converting duration into minutes 
    mins = int(int(talk['duration'])/60)
	
	#How many sentences in X min
    sentences_per_min = int(len(sentences)/mins)

    print('sentences_per_min',sentences_per_min)

	#chunking the big list of sentences into that amount
    sentences_grouped = chunk(sentences,sentences_per_min)
	#turning it into a regular old list of lists
    sentences_grouped = list(sentences_grouped)

    minute = 1
    for sentences_group in sentences_grouped:
        sentences_group_joined = " ".join(sentences_group)


        print('------------')
        print(sentences_group_joined)
        print('------------')
        response = analyze_text_sentiment(sentences_group_joined)
        print(response)
        sentimentsdf = sentimentsdf.append({"title":talk["title"],
                                    "url":talk["url"],
                                    "transcript":sentences_group_joined, 
                                    "minute":minute, 
                                    "score":response["score"], 
                                    "magnitude":response["magnitude"]}, ignore_index=True)
        print(sentimentsdf)
        minute +=1

sentimentsdf.to_csv("minutewise_sentiment.csv")