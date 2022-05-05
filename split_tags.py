import pandas as pd

df = pd.read_csv ("transcript_sentiments.csv")

master_list = df["tags"].tolist()

open_list = []

clean_df = pd.DataFrame()
clean_df['tags'] = df['tags']
clean_df['views'] = df['views']

#cleaning the column
for idx,item in df["tags"].iteritems():
    # print(idx, item)
    tempList = item.replace("[","").replace("'","").replace("]","").split(",") 
    tempList = [x.lower().strip() for x in tempList]
    clean_df['tags'][idx] = tempList
    open_list = open_list + clean_df['tags'][idx]

open_list1 = []
for item in open_list:
    open_list1.append(item.strip().lower())

unique_tags = list(set(open_list1))

view_count = {item:0 for item in unique_tags}

#normalizing the column by dividing views by the number of the tags
for idx,item in df["views"].iteritems():
    normalized_views = df["views"][idx]/len(clean_df["tags"][idx])
    for tag in clean_df['tags'][idx]:
        view_count[tag] += normalized_views

view_count = {k: v for k, v in sorted(view_count.items(), key=lambda item: item[1])}
print(view_count)

#saving the file
with open('view_count.csv', 'w') as f:
    f.write("%s,%s\n"%("Tag","Views"))
    for key in view_count.keys():
        f.write("%s,%s\n"%(key,view_count[key]))