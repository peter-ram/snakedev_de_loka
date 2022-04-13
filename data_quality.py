import sqlite3
import pandas as pd
import sys

month_string = sys.argv[1]
#month_string = "202202"


con = sqlite3.connect('bikes-warehouse.db')
table_name = "bikes"
string = "datalake//JC-" + month_string + "-citibike-tripdata.csv"

query = """SELECT * FROM bikes WHERE period = {}""".format(month_string)
if con is not None:
    c = con.cursor()
    c.execute(query)
    rows = c.fetchall()
    names = list(map(lambda x: x[0], c.description))
    data = pd.DataFrame(rows, columns = names)
    
    
# performing data quality tests

# check if start date > end date

condition = data.started_at > data.ended_at

date_results = data[condition]

if date_results.shape[0] != 0:
    raise Exception("Something is wrong with the data: there are start dates > end dates")

print("dates test successful")

# column integrity test
column_to_test = "start_station_name"

null_percentage = 100*data[column_to_test].isnull().sum(axis = 0)/data[column_to_test].count()
if null_percentage > 10.0:
    raise Exception("Something is wrong with the data: more than 10% nulls")
    
print("null percentage is ", null_percentage)