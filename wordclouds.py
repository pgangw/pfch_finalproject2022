import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# nltk.download('stopwords')
from nltk.corpus import stopwords

stop = stopwords.words('english')

sentiments_df = pd.read_csv("title_sentiments.csv")
sentiments_df = sentiments_df.sort_values("views", ascending=False, ignore_index=True)
sentiments_df["ttranscript_stop"] = sentiments_df["ttranscript"].map(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))

sentiments_df = pd.read_csv("transcript_sentiments.csv")
sentiments_df = sentiments_df.sort_values("views", ascending=False, ignore_index=True)

sentiments_df["title_stop"] = sentiments_df["title"].map(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))


###WORDCLOUDS OF TRANSCRIPTS### 
###top 20 views 
text = ""
print(sentiments_df.loc[0:20,:])
for idx, row in sentiments_df.loc[0:20,:].iterrows():
    # print(idx)
    # print(row)
    text = text + row["ttranscript_stop"]
    # print(len(text))
wordcloud = WordCloud(background_color="white", colormap='Reds').generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

###bottom 20 views 
text = ""
# print(sentiments_df.loc[0:20,:])
for idx, row in sentiments_df.loc[-20:,:].iterrows():
    text = text + row["ttranscript_stop"]
wordcloud = WordCloud(background_color="white", colormap='Reds').generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


###WORDCLOUDS OF TITLES### 
###top 20 views
text = ""
print(sentiments_df.loc[0:20,:])
for idx, row in sentiments_df.loc[0:20,:].iterrows():
    text = text + row["title_stop"]
wordcloud = WordCloud(background_color="white", colormap='Reds').generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

#bottom 20 views
text = ""
for idx, row in sentiments_df.loc[-20:,:].iterrows():
    text = text + row["title_stop"]
wordcloud = WordCloud(background_color="white", colormap='Reds').generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()