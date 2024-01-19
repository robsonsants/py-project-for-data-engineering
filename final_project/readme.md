# Project Overview
A multi-national firm has hired you as a data engineer. Your job is to access and process data as per requirements.

Your boss asked you to compile the list of the top 10 largest banks in the world ranked by market capitalization in billion USD. Further, you need to transform the data and store it in USD, GBP, EUR, and INR per the exchange rate information made available to you as a CSV file. You should save the processed information table locally in a CSV format and as a database table. Managers from different countries will query the database table to extract the list and note the market capitalization value in their own currency.

# Directions
1. Write a function to extract the tabular information from the given URL under the heading By Market Capitalization, and save it to a data frame.
2. Write a function to transform the data frame by adding columns for Market Capitalization in GBP, EUR, and INR, rounded to 2 decimal places, based on the exchange rate information shared as a CSV file.
3. Write a function to load the transformed data frame to an output CSV file.
4. Write a function to load the transformed data frame to an SQL database server as a table.
5. Write a function to run queries on the database table.
6. Run the following queries on the database table:
    a. Extract the information for the London office, that is Name and MC_GBP_Billion
    b. Extract the information for the Berlin office, that is Name and MC_EUR_Billion
    c. Extract the information for New Delhi office, that is Name and MC_INR_Billion
7. Write a function to log the progress of the code.
8. While executing the data initialization commands and function calls, maintain appropriate log entries.

## Acquiring and Processing Information on the World's Largest Banks

# Project Scenario:

You have been hired as a data engineer by research organization. Your boss has asked you to create a code that can be used to compile the list of the top 10 largest banks in the world ranked by market capitalization in billion USD. Further, the data needs to be transformed and stored in GBP, EUR and INR as well, in accordance with the exchange rate information that has been made available to you as a CSV file. The processed information table is to be saved locally in a CSV format and as a database table.

Your job is to create an automated system to generate this information so that the same can be executed in every financial quarter to prepare the report.

Particulars of the code to be made have been shared below.

| Parameter | Value |
| ------ | ------ |
| Code name | banks_project.py |
| Data URL | https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks |
| Exchange rate CSV path | https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv |
| Table Attributes (upon Extraction only) | Name, MC_USD_Billion |
| Table Attributes (final) | Name, MC_USD_Billion, MC_GBP_Billion, MC_EUR_Billion, MC_INR_Billion |
| Output CSV Path | ./Largest_banks_data.csv |
| Database name | Banks.db |
| Table name | Largest_banks |
| Log file | code_log.txt |


# Project tasks

Task 1:
Write a function *log_progress()* to log the progress of the code at different stages in a file *code_log.txt*. Use the list of log points provided to create log entries as every stage of the code.

Task 2:
Analyze the webpage on the given URL:

```sh
https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks
```

Identify the position of the required table under the heading *By market capitalization*. Write the function *extract()* to retrieve the information of the table to a Pandas data frame.

Note: Remember to remove the last character from the *Market Cap* column contents, like, '\n', and typecast the value to float format.

Write a function call for *extract()* and print the returning data frame.

Make the relevant log entry.


Task 3:
Transform the dataframe by adding columns for Market Capitalization in GBP, EUR and INR, rounded to 2 decimal places, based on the exchange rate information shared as a CSV file.
a. Write the code for a function *transform()* to perform the said task.
b. Execute a function call to *transform()* and verify the output.

The Transform function needs to perform the following tasks:

1. Read the exchange rate CSV file and convert the contents to a dictionary so that the contents of the first columns are the keys to the dictionary and the contents of the second column are the corresponding values.

2. Add 3 different columns to the dataframe, viz. *MC_GBP_Billion*, *MC_EUR_Billion* and *MC_INR_Billion*, each containing the content of *MC_USD_Billion* scaled by the corresponding exchange rate factor. Remember to round the resulting data to 2 decimal places.

A sample statement is being provided for adding the *MC_GBP_Billion* column. You can use this to add the other two statements on your own.

```sh
df['MC_GBP_Billion'] = [np.round(x*exchange_rate['GBP'],2) for x in df['MC_USD_Billion']]
```

Write the function call for *transform()* and print the contents of the returning data frame. Comment out all previous print statements.

Make the relevant log entry and execute the code.

Task 4:
Load the transformed dataframe to an output CSV file. Write a function *load_to_csv()*, execute a function call and verify the output.

Task 5:
Write the function to load the transformed data frame to an SQL database, like, *load_to_db()*. Use the database and table names as mentioned in the project scenario.

Before calling this function, initiate the connection to the SQLite3 database server with the name *Banks.db*. Pass this connection object, along with the required table name *Largest_banks* and the transformed data frame, to the *load_to_db()* function in the function call.

Make the relevant log entry.

Task 6:
Write the function *run_queries()* that accepts the query statement, and the SQLite3 Connection object, and generates the output of the query. The query statement should be printed along with the query output.

Execute 3 function calls using the queries as mentioned below.

1. Print the contents of the entire table
Query statement:

```sh
SELECT * FROM Largest_banks
```

2. Print the average market capitalization of all the banks in Billion USD.
Query statement:

```sh
SELECT AVG(MC_GBP_Billion) FROM Largest_banks
```
3. Print only the names of the top 5 banks
Query statement:

```sh
SELECT Name from Largest_banks LIMIT 5
```
Make the relevant log entry.

Task 7:
After updating all the *log_progress()* function calls, you have to run the code for a final execution. However, you will first have to remove the *code_log.txt* file, that would have been created and updated throughout the multiple executions of the code in this lab. You may remove the file using the following command on a terminal.

```sh
rm code_log.txt
```

# Conclusion

With this, you are now trained to perform ETL operations on real-world data and make the processed information available for further use in different formats.

You should now be able to:

- Use Webscraping techniques to extract information from any website as per requirement.

- Use Pandas data frames and dictionaries to transform data as per requirement.

- Load the processed information to CSV files and as Database tables

- Query the database tables using SQLite3 and pandas libraries

- Log the progress of the code properly

