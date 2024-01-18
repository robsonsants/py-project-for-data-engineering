import sqlite3
import pandas as pd

conn = sqlite3.connect('STAFF.db')

#creating the table
table_name = 'Departments'
attribute_list = ['DEPT_ID', 'DEP_NAME', 'MANAGER_ID', 'LOC_ID']

#reading the csv file
file_path = 'C:/Users/allis/Downloads/py-project-for-data-engineering/scripts/acessing_dbs/Departments.csv'
df = pd.read_csv(file_path, names = attribute_list)

#loading the data to a table
df.to_sql(table_name, conn, if_exists = 'replace', index =False)
print('Table is ready')

# data retrieval on the database
# viewing all the data in the table
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

#viewing only DEP_NAME column of data
query_statement = f"SELECT DEP_NAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

#viewing the total number of entries in the table
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

#appending some data to the table.
data_dict = {'DEPT_ID' : [9],
            'DEP_NAME' : ['Quality Assurance'],
            'MANAGER_ID' : [30010],
            'LOC_ID' : ['L0010']}
data_append = pd.DataFrame(data_dict)

data_append.to_sql(table_name, conn, if_exists = 'append', index =False)
print('Data appended successfully')

#Before proceeding with the final execution, you need to add the command to close the connection to the database after all the queries are executed.
conn.close()