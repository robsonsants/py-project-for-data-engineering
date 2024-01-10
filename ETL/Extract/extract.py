import glob
import pandas as pd
import numpy as np
from datetime import datetime

list_csv=glob('*.csv')
list_csv:['source1.csv', 'source2.csv', 'source3.csv']

list_json = glob.glob('*.json')
list_json:['source1.json', 'source3.json', 'source2.json']

def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe

df = extract_from_csv('source1.csv')

def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process,lines=True)
    return dataframe

df = extract_from_json('source1.json')

def extract():

    #create and empty data frame to hold extracted data
    extracted_data = pd.DataFrame(columns=['name','height','weight'])

    #process all csv files
    for csvfile in glob.glob("*.csv"):
        extracted_data = extracted_data.append(extract_from_csv(csvfile),
        ignore_index=True)
    
    #process all json files
    for jsonfile in glob.glob("*.json"):
        extracted_data = extracted_data.append(extract_from_json(jsonfile),
        ignore_index=True)
    
    return extracted_data

#df = extract_from_csv('source.csv')

def transform(data):
    #convert height which is in inches to millimeter
    #convert inches to meters and round off to two decimals
    #(one inch is 0.0254 meters)
    data['height'] = round(data.height * 0.0254,2)

    #convert pounds to kilograms and round of to two decimals
    #(one pound is 0.45359237 kilograms)
    data['weight'] = round(data.weight * 0.45359237)
    return data

targetfile = "*.csv"
def load(targetfile, data_to_load):
    data_to_load.to_csv(targetfile)

    targetfile = "transformed_data.csv"

    load(targetfile, transformed_data)

#Logging Entries
    
def log(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("logfile.txt", "a") as f:
        f.write ( timestamp + ',' + message + '\n')


#FINAL CALL 

log (" ETL Job Started")

log (" Extract phase Started")
extracted_data = extract()
log (" Extract phase Ended")

log (" Transform Job Started")
transformed_data = transform(extracted_data)
log (" Transform phase Ended")

log (" Load Job Started")
load(targetfile, transformed_data)
log (" Load phase Ended")

log (" ETL phase Ended")