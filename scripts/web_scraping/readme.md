# Objetives:
By the end of this lab, you will be able to:
1. Use the requests and BeautifulSoup libraries to extract the contents of a web page
2. Analyze the HTML code of a webpage to find the relevant information
3. Extract the relevant information and save it in the required form

# Scenario
Consider that you have been hired by a Multiplex management organization 
to extract the information of the top 50 movies with the best average rating 
from the web link shared below.

# https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films

The information required is Average Rank, Film, and Year.
You are required to write a Python script webscraping_movies.py that extracts the 
information and saves it to a CSV file top_50_films.csv. You are also required  to save the same information to a database Movies.db under the table name Top_50.

# Initial Steps

You require the following libraries for this lab.

1. pandas library for data storage and manipulation.

2. BeautifulSoup library for interpreting the HTML document.

3. requests library to communicate with the web page.

4. sqlite3 for creating the database instance.

While requests and sqlite3 come bundled with Python3, you need to install pandas and BeautifulSoup libraries to the IDE.

For this, run the following commands in a terminal window.

```sh
python3.11 -m pip install pandas
python3.11 -m pip install bs4
```

# to run the code 

```sh
python webscraping_movies.py
```