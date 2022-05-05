import pandas as pd
import matplotlib.pyplot as plt


###Top 10 most viwed videos and their titles
sentiments_df = pd.read_csv('title_sentiments.csv')
sentiments_df = sentiments_df.sort_values("views", ascending=False, ignore_index=True).loc[0:9,:]
plt.plot(sentiments_df['title'], sentiments_df['views'])
plt.xticks(rotation=30, fontsize='6')
plt.tight_layout()
plt.show()

Title = sentiments_df['title'].head(10)
Views = sentiments_df['views'].head(10)
 
# Figure Size
fig, ax = plt.subplots(figsize =(16, 9))
 
# Horizontal Bar Plot
ax.barh(Title, Views, color=['red'])
 
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
plt.yticks(rotation=45, fontsize='5', fontweight ='bold')
 
# Add annotation to bars
for i in ax.patches:
    plt.text(i.get_width()+0.2, i.get_y()+0.5,
             str(round((i.get_width()), 2)),
             fontsize = 10, fontweight ='bold',
             color ='grey')
 
# Add Plot Title
ax.set_title('Most viewed Ted Talks',
             loc ='left', fontweight ='bold')
 
# Add Text watermark
fig.text(0.9, 0.15, 'pfch2022', fontsize = 12,
         color ='grey', ha ='right', va ='bottom',
         alpha = 0.7)      

plt.xlabel('Views (in million)')
plt.ylabel('Title')        
 
# Show Plot
plt.show()



###Top 10 least viewed videos and their titles
sentiments_df = pd.read_csv('title_sentiments.csv')
sentiments_df = sentiments_df.sort_values("views", ascending=True, ignore_index=True).loc[0:9,:]
plt.plot(sentiments_df['title'], sentiments_df['views'])
plt.xticks(rotation=30, fontsize='6')
plt.tight_layout()
plt.show()

Title = sentiments_df['title'].head(10)
Views = sentiments_df['views'].head(10)
 
# Figure Size
fig, ax = plt.subplots(figsize =(16, 9))
 
# Horizontal Bar Plot
ax.barh(Title, Views, color=['red'])
 
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
plt.yticks(rotation=45, fontsize='5', fontweight ='bold')
 
# Add annotation to bars
for i in ax.patches:
    plt.text(i.get_width()+0.2, i.get_y()+0.5,
             str(round((i.get_width()), 2)),
             fontsize = 10, fontweight ='bold',
             color ='grey')
 
# Add Plot Title
ax.set_title('Least viewed Ted Talks',
             loc ='left', fontweight ='bold')
 
# Add Text watermark
fig.text(0.9, 0.15, 'pfch2022', fontsize = 12,
         color ='grey', ha ='center', va ='bottom',
         alpha = 0.7)      
 
plt.xlabel('Views (in million)')
plt.ylabel('Title')      

# Show Plot
plt.show()


