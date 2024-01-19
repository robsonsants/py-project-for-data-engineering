import requests
import sqlite3
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup  
from datetime import datetime 

def extract(url, table_attribs):
    page = requests.get(url).text
    data = BeautifulSoup(page, 'html.parser')
    df_list = []  #list of DataFrames
    df = pd.DataFrame(columns=table_attribs)
    tables = data.find_all('tbody')
    rows = tables[0].find_all('tr')
    for row in rows:
        col = row.find_all('td')
        if col and len(col) > 1:
            #look for the second 'a' to get the name of the bank
            bank_name = col[1].find_all('a')[1].contents[0] if len(col[1].find_all('a')) > 1 else None
            #tries to convert the value to float, which would implicitly discard the '\n' if the value was formatted correctly.
            market_cap = col[2].contents[0].replace(',', '').replace('B', '') if len(col[2].contents) > 0 else None

            #attempt to convert market capitalization to float
            try:
                market_cap = float(market_cap) if market_cap is not None else None
            except ValueError:
                market_cap = None

            data_dict = {"Name": bank_name,
                        "MC_USD_Billion": market_cap}

            df1 = pd.DataFrame([data_dict], columns=table_attribs)
            df_list.append(df1)

    #Concatenate the list's DataFrames into a single DataFrame
    df = pd.concat(df_list, ignore_index=True)

    return df

def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open("./code_log.txt","a") as f: 
        f.write(timestamp + ' : ' + message + '\n')

url = 'https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs = ["Name", "MC_USD_Billion"]
db_name = 'Banks.db'
table_name = 'Largest_banks'
csv_path = './Largest_banks_data.csv'

df = extract(url, table_attribs)
print(df)

log_progress("Data extracted from the 'By market capitalization' table and loaded into a DataFrame.")


