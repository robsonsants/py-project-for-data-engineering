# Objectives
In this lab you'll learn how to:
1. Create a database using Python
2. Load the data from a CSV file as a table to the database
3. Run basic "queries" on the database to access the information

# Scenario
Consider a dataset of employee records that is available with an HR team in a CSV file.  As a Data Engineer, you are required to create the database called STAFF and load the contents  of the CSV file as a table called INSTRUCTORS. The headers of the available data are:

| Header | Description |
| ------ | ------ |
| ID | Employee ID |
| FNAME | First Name |
| LNAME | Last Name |
| CITY | City of residence |
| CCODE | Country code (2 letters) |

# Setting Up
Usually, the database for storing data would be created on a server to which the other team members would have access. For the purpose of this lab, we are going to create the database on a dummy server using SQLite3 library.

Note: SQLite3 is a software library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine. SQLite is the most widely deployed SQL database engine in the world. SQLite3 comes bundled with Python and does not require installation.

# Initial steps

For this lab, you will need a Python file in the project folder. You can name it db_code.py.

Run the following command in the terminal. Make sure the current directory /home/project/.

wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/INSTRUCTOR.csv

If you dont have pandas installed, install: 

```sh
python3.11 -m pip install pandas
```

# Python Scripting: Database initiation 

Let us first create a database using Python.

Open db_code.py and import the sqlite3 library using the below mentioned command.

```sh
import sqlite3
```

Import the pandas library in db_code.py using the following code.

```sh
import pandas as pd
```
Now, you can use SQLite3 to create and connect your process to a new database STAFF using the following statements.

```sh
conn = sqlite3.connect('STAFF.db')
```

# Code Execution
Execute db_code.py from the terminal window using the following command.

```sh
python3.11 db_code.py
```

## practice

1. In the same database STAFF, create another table called Departments. The attributes of the table are as shown below.

| Header | Description |
| ------ | ------ |
| DEPT_ID | Department ID |
| DEP_NAME | Department Name |
| MANAGER_ID | Manager ID |
| LOC_ID | Location ID |

2. Populate the Departments table with the data available in the CSV file which can be downloaded from the link below using wget.

https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/Departments.csv

3. Append the Departments table with the following information.

| Attribute | Value |
| ------ | ------ |
| DEPT_ID | 9 |
| DEP_NAME | Quality Assurance |
| MANAGER_ID | 30010 |
| LOC_ID | L0010 |

4. Run the following queries on the Departments Table:
a. View all entries
b. View only the department names
c. Count the total entries