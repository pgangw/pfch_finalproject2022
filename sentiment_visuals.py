import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

sentiments_df = pd.read_csv('master_all_sentiments.csv')
sentiments_df = sentiments_df.sort_values("views", ascending=False, ignore_index=True).loc[0:9,:]

transcript_score = sentiments_df['score'].head(10)
Views = sentiments_df['views'].head(10)
fig, ax = plt.subplots(figsize =(10, 3))

###PLOTTING SENTIMENT SORES OF ALL THE COLUMNS
title = sentiments_df['title_x'].values
x = np.arange(len(title))
w = 0.3
plt.bar(x-w, sentiments_df['score'].values, width=w, label='Transcript Score', color=['#E85D04'])
plt.bar(x, sentiments_df['tscore'].values, width=w, label='Title Score', color=['red'])
plt.bar(x+w, sentiments_df['dscore'].values, width=w, label='Description Score', color=['#FFBA08'])
plt.xticks(x, title)
plt.ylim([-1,1])
plt.tight_layout()
plt.xlabel('Title')
plt.ylabel('Sentiment Scores')
plt.legend()

plt.xticks(rotation=20, fontsize='6', fontweight="bold")

fig.text(0.9, 0.15, 'pfch2022', fontsize = 12,
         color ='grey', ha ='left', va ='bottom',
         alpha = 0.7)   

ax.set_title('Sentiment scores of the top 10 talks (based on views)',
             loc ='left', fontweight ='bold')        

plt.show()



##PLOTTING SENTIMENT SORES OF ALL MAGNITUDES
transcript_score = sentiments_df['score'].head(10)
Views = sentiments_df['views'].head(10)
fig, ax = plt.subplots(figsize =(10, 3))

title = sentiments_df['title_x'].values
x = np.arange(len(title))
w = 0.3
plt.bar(x-w, sentiments_df['magnitude'].values, width=w, label='Transcript Score', color=['#E85D04'])
plt.bar(x, sentiments_df['tmagnitude'].values, width=w, label='Title Score', color=['red'])
plt.bar(x+w, sentiments_df['dmagnitude'].values, width=w, label='Description Score', color=['#FFBA08'])
plt.xticks(x, title)
plt.ylim([0,500])
plt.tight_layout()
plt.xlabel('Title')
plt.ylabel('Magnitude')
plt.legend()
# plt.savefig("CSVBarplots.png", bbox_inches="tight")

plt.xticks(rotation=20, fontsize='6', fontweight="bold")

fig.text(0.9, 0.15, 'pfch2022', fontsize = 12,
         color ='grey', ha ='left', va ='bottom',
         alpha = 0.7)   

ax.set_title('Magnitude of the top 10 talks (based on views)',
             loc ='left', fontweight ='bold')        

plt.show()



###PLOTTING MAGNITUDES OF DESCRIPTIONS AND VIEWS BECAUSE THE ABOVE VISUAL IS DIFFICULT TO READ

Title = sentiments_df['title_x'].head(10)
Magnitude = sentiments_df['tmagnitude'].head(10)
 
# Figure Size
fig, ax = plt.subplots(figsize =(16, 9))
 
# Horizontal Bar Plot
ax.barh(Title, Magnitude, color=['#FFBA08'])
 
# Remove axes splines
for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)
 
# Remove x, y Ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
 
# Add padding between axes and labels
ax.xaxis.set_tick_params(pad = 5)
ax.yaxis.set_tick_params(pad = 10)
 
# Add x, y gridlines
ax.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)
 
# Show top values
ax.invert_yaxis()

# Rotate y axis labels
plt.yticks(rotation=45, fontsize='4.5', fontweight ='bold')
 
# Add annotation to bars
for i in ax.patches:
    plt.text(i.get_width(), i.get_y()+0.5,
             str(round((i.get_width()), 2)),
             fontsize = 10, fontweight ='bold',
             color ='grey')
 
# Add Plot Title
ax.set_title('Magnitude of the desciptions of the top 10 talks',
             loc ='left', fontweight ='bold')
 
# Add Text watermark
fig.text(0.9, 0.15, 'pfch2022', fontsize = 12,
         color ='grey', ha ='right', va ='bottom',
         alpha = 0.7)    

plt.xlabel('Magnitude')
plt.ylabel('Title')           
 
# Show Plot
plt.show()



###MAGNITUDES OF TITLES AND VIEWS

Title = sentiments_df['title_x'].head(10)
Magnitude = sentiments_df['dmagnitude'].head(10)
 
# Figure Size
fig, ax = plt.subplots(figsize =(16, 9))
 
# Horizontal Bar Plot
ax.barh(Title, Magnitude, color=['red'])
 
# Remove axes splines
for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)
 
# Remove x, y Ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
 
# Add padding between axes and labels
ax.xaxis.set_tick_params(pad = 5)
ax.yaxis.set_tick_params(pad = 10)
 
# Add x, y gridlines
ax.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)
 
# Show top values
ax.invert_yaxis()

# Rotate y axis labels
plt.yticks(rotation=45, fontsize='4.5', fontweight ='bold')
 
# Add annotation to bars
for i in ax.patches:
    plt.text(i.get_width(), i.get_y()+0.5,
             str(round((i.get_width()), 2)),
             fontsize = 10, fontweight ='bold',
             color ='grey')
 
# Add Plot Title
ax.set_title('Magnitude of the titles of the top 10 talks',
             loc ='left', fontweight ='bold')
 
# Add Text watermark
fig.text(0.9, 0.15, 'pfch2022', fontsize = 12,
         color ='grey', ha ='right', va ='bottom',
         alpha = 0.7)      

plt.xlabel('Magnitude')
plt.ylabel('Title')           
 
# Show Plot
plt.show()



###SENTIMENT SCORES OF THE LEAST VIEWED VIEWS

sentiments_df = pd.read_csv('master_all_sentiments.csv')
sentiments_df = sentiments_df.sort_values("views", ascending=True, ignore_index=True).loc[0:9,:]

transcript_score = sentiments_df['score'].head(10)
Views = sentiments_df['views'].head(10)
fig, ax = plt.subplots(figsize =(10, 3))

title = sentiments_df['title_x'].values
x = np.arange(len(title))
w = 0.3
plt.bar(x-w, sentiments_df['score'].values, width=w, label='Transcript Score', color=['#E85D04'])
plt.bar(x, sentiments_df['tscore'].values, width=w, label='Title Score', color=['red'])
plt.bar(x+w, sentiments_df['dscore'].values, width=w, label='Description Score', color=['#FFBA08'])
plt.xticks(x, title)
plt.ylim([-1,1])
plt.tight_layout()
# plt.xlabel('Titles')
plt.legend()
# plt.savefig("CSVBarplots.png", bbox_inches="tight")

plt.xticks(rotation=20, fontsize='6', fontweight="bold")

fig.text(0.9, 0.15, 'pfch2022', fontsize = 12,
         color ='grey', ha ='center', va ='bottom',
         alpha = 0.7)   

ax.set_title('Sentiment scores of the bottom 10 talks (based on views)',
             loc ='left', fontweight ='bold')    

plt.xlabel('Title')
plt.ylabel('Sentiment Scores')   

plt.show()



###ALL MAGNITUDES
transcript_score = sentiments_df['score'].head(10)
Views = sentiments_df['views'].head(10)
fig, ax = plt.subplots(figsize =(10, 3))

title = sentiments_df['title_x'].values
x = np.arange(len(title))
w = 0.3
plt.bar(x-w, sentiments_df['magnitude'].values, width=w, label='Transcript Score', color=['#E85D04'])
plt.bar(x, sentiments_df['tmagnitude'].values, width=w, label='Title Score', color=['red'])
plt.bar(x+w, sentiments_df['dmagnitude'].values, width=w, label='Description Score', color=['#FFBA08'])
plt.xticks(x, title)
plt.ylim([0,500])
plt.tight_layout()
plt.xlabel('Title')
plt.ylabel('Magnitude')
plt.legend()

plt.xticks(rotation=20, fontsize='6', fontweight="bold")

fig.text(0.9, 0.15, 'pfch2022', fontsize = 12,
         color ='grey', ha ='center', va ='bottom',
         alpha = 0.7)   

ax.set_title('Magnitude of the bottom 10 talks (based on views)',
             loc ='left', fontweight ='bold')        

plt.xlabel('Title')
plt.ylabel('Views')   

plt.show()



###MAGNITUDES OF DESCRIPTIONS AND VIEWS

Title = sentiments_df['title_x'].head(10)
Magnitude = sentiments_df['tmagnitude'].head(10)
 
# Figure Size
fig, ax = plt.subplots(figsize =(16, 9))
 
# Horizontal Bar Plot
ax.barh(Title, Magnitude, color=['#FFBA08'])
 
# Remove axes splines
for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)
 
# Remove x, y Ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
 
# Add padding between axes and labels
ax.xaxis.set_tick_params(pad = 5)
ax.yaxis.set_tick_params(pad = 10)
 
# Add x, y gridlines
ax.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)
 
# Show top values
ax.invert_yaxis()

# Rotate y axis labels
plt.yticks(rotation=45, fontsize='4.5', fontweight ='bold')
 
# Add annotation to bars
for i in ax.patches:
    plt.text(i.get_width(), i.get_y()+0.5,
             str(round((i.get_width()), 2)),
             fontsize = 10, fontweight ='bold',
             color ='grey')
 
# Add Plot Title
ax.set_title('Magnitude of the desciptions of the bottom 10 talks',
             loc ='left', fontweight ='bold')
 
# Add Text watermark
fig.text(0.9, 0.15, 'pfch2022', fontsize = 12,
         color ='grey', ha ='right', va ='bottom',
         alpha = 0.7)    

plt.xlabel('Magnitude')
plt.ylabel('Title')           
 
# Show Plot
plt.show()



###MAGNITUDES OF TITLES AND VIEWS

Title = sentiments_df['title_x'].head(10)
Magnitude = sentiments_df['dmagnitude'].head(10)
 
# Figure Size
fig, ax = plt.subplots(figsize =(16, 9))
 
# Horizontal Bar Plot
ax.barh(Title, Magnitude, color=['red'])
 
# Remove axes splines
for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)
 
# Remove x, y Ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
 
# Add padding between axes and labels
ax.xaxis.set_tick_params(pad = 5)
ax.yaxis.set_tick_params(pad = 10)
 
# Add x, y gridlines
ax.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)
 
# Show top values
ax.invert_yaxis()

# Rotate y axis labels
plt.yticks(rotation=45, fontsize='4.5', fontweight ='bold')
 
# Add annotation to bars
for i in ax.patches:
    plt.text(i.get_width(), i.get_y()+0.5,
             str(round((i.get_width()), 2)),
             fontsize = 10, fontweight ='bold',
             color ='grey')
 
# Add Plot Title
ax.set_title('Magnitude of the titles of the bottom 10 talks',
             loc ='left', fontweight ='bold')
 
# Add Text watermark
fig.text(0.9, 0.15, 'pfch2022', fontsize = 12,
         color ='grey', ha ='right', va ='bottom',
         alpha = 0.7)      

plt.xlabel('Magnitude')
plt.ylabel('Title')           
 
# Show Plot
plt.show()