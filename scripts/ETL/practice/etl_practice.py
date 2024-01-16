import glob 
import pandas as pd 
import xml.etree.ElementTree as ET 
from datetime import datetime 

log_file = "log_file.txt" 
target_file = "transformed_data.csv"

def extract_from_csv(file_to_process): 
    dataframe = pd.read_csv(file_to_process) 
    return dataframe 

def extract(): 
    extracted_data = pd.DataFrame(columns=['car_model','year_of_manufacture','price', 'fuel'])  
# create an empty data frame to hold extracted data
    # process all csv files 
    for csvfile in glob.glob("*.csv"): 
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(csvfile))], ignore_index=True)
         
    return extracted_data 

def load_data(target_file, transformed_data): 
    transformed_data.to_csv(target_file)

def log_progress(message): 
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open(log_file,"a") as f: 
        f.write(timestamp + ',' + message + '\n') 

def transform(data): 
    # Convert inches to meters and round off to two decimals 
    # 1 inch is 0.0254 meters 
    data['price'] = round(data.price, 2)   
    return data 

# Log the initialization of the ETL process 
log_progress("ETL Job Started") 
  
# Log the beginning of the Extraction process 
log_progress("Extract phase Started") 
extracted_data = extract() 
  
# Log the completion of the Extraction process 
log_progress("Extract phase Ended") 
  
# Log the beginning of the Transformation process 
log_progress("Transform phase Started") 
transformed_data = transform(extracted_data) 
print("Transformed Data") 
print(transformed_data) 
  
# Log the completion of the Transformation process 
log_progress("Transform phase Ended") 
  
# Log the beginning of the Loading process 
log_progress("Load phase Started") 
load_data(target_file,transformed_data) 
  
# Log the completion of the Loading process 
log_progress("Load phase Ended") 
  
# Log the completion of the ETL process 
log_progress("ETL Job Ended") 

#In this lab, I practiced the implementation of:
#Extraction of data from CSV, JSON, and XML file formats.
#Transformation of data as per requirement.
#Loading the transformed data to a CSV file.
#Logging the progress of the said operations.