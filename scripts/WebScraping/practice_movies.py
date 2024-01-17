#Try the following practice problems to test your understanding of the lab. 
#Please note that the solutions for the following are not shared. 
#You are encouraged to use the discussion forums in case you need help.

#1.Modify the code to extract Film, Year, and Rotten Tomatoes' Top 100 headers.

#2.Restrict the results to only the top 25 entries.

#3.Filter the output to print only the films released in the 2000s (year 2000 included).

import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'Movies.db'
table_name = 'Top_50'
csv_path = 'C:/Users/allis/Downloads/py-project-for-data-engineering/scripts/WebScraping/top_50_films.csv'
df = pd.DataFrame(columns=["Film","Year","Rotten Tomatoes' Top 100 headers"])
count = 0

html_page = requests.get(url).text
data = BeautifulSoup(html_page, 'html.parser')

tables = data.find_all('tbody')
rows = tables[0].find_all('tr')

for row in rows:
    if count<25:
        col = row.find_all('td')
        if len(col)!=0:
            data_dict = {"Film": col[1].contents[0],
                         "Year": col[2].contents[0],
                         "Rotten Tomatoes' Top 100 headers": col[3].contents[0]}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df,df1], ignore_index=True)
            count+=1
    else:
        break

print(df)

#Assuming df is your DataFrame that you've created from the scraped data
#Convert the 'Year' column to integer
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

#Filter the DataFrame for movies released in the 2000s
df_2000s = df[(df['Year'] >= 2000) & (df['Year'] <= 2009)]

print(df_2000s)