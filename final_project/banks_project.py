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

    #concatenate the list's DataFrames into a single DataFrame
    df = pd.concat(df_list, ignore_index=True)

    return df

def transform(df):
    rate_df = pd.read_csv('exchange_rate.csv')
    exchange_rate = rate_df.set_index('Currency').to_dict()['Rate']

    #adding new columns with converted and rounded values
    df['MC_GBP_Billion'] = [np.round(x*exchange_rate['GBP'],2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion'] = [np.round(x*exchange_rate['EUR'],2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x*exchange_rate['INR'],2) for x in df['MC_USD_Billion']]

    return df

def load_to_csv(df, csv_path):
    df.to_csv(csv_path)

def load_to_db(df, sql_connection, table_name):
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)

def run_query(query_statement, sql_connection):
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)

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

log_progress('Initiating Transformation process')

transformed_df = transform(df)
print(transformed_df)

#printing the market capitalization value of the fifth largest bank in EUR billions
fifth_bank_eur_mc = transformed_df['MC_EUR_Billion'][4]
print(fifth_bank_eur_mc)

log_progress('Data transformation complete. Initiating loading process')

load_to_csv(df, csv_path)

log_progress('Data saved to CSV file')

sql_connection = sqlite3.connect('Banks.db')

log_progress('SQL Connection initiated.')

load_to_db(df, sql_connection, table_name)

log_progress('Data loaded to Database as table. Running the query')

#Print the contents of the entire table
query_statement = f"SELECT * FROM {table_name}"
run_query(query_statement, sql_connection)

#Print the average market capitalization of all the banks in Billion USD.
query_statement = f"SELECT AVG(MC_GBP_Billion) FROM {table_name}"
run_query(query_statement, sql_connection)

#Print only the names of the top 5 banks
query_statement = f"SELECT Name from {table_name} LIMIT 5"
run_query(query_statement, sql_connection)

log_progress('Process Complete.')