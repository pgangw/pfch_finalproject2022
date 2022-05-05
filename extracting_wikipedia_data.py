from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


df = pd.read_csv ("transcript_sentiments.csv")
final_df = df.sort_values(by=['views'], ascending=False)

#cleaning the coloumn
final_df['clean_name'] = df['main_speaker'].replace(" ", "_", regex=True)
with open('output.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["Header", "Value"])

#requesting from wikipedia
i = 0
for clean_name in final_df['clean_name']:
    page = requests.get('https://en.wikipedia.org/wiki/' + clean_name)
    print(clean_name)
    print(page.status_code)

    soup = BeautifulSoup(page.content, 'html.parser')

    try: 
        table = soup.find('table')
        rows = table.find_all('tr')
        print(clean_name, "FOUND")
    except:
        continue
    
    with open('output.csv', 'a', newline="") as f:
        writer = csv.writer(f)
        for tr in rows:
            try:
                th = tr.find('th').get_text()
                td = tr.find('td').get_text()
                if ('Nationality' in th):
                    print('Found born in', clean_name)
                    writer.writerow(['Name', clean_name.replace("_", " ")])
                    writer.writerow([th, td])
                    i+=1
                    break
            except:
                continue  
    
#extracting details of 100 speakers
    print('At i',i)
    if i==100:
        break



