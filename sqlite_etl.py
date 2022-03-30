import sqlite3
import pandas as pd
import sys

# turn into script input
month_string = sys.argv[1]

con = sqlite3.connect('bikes-warehouse.db')

table_name = "bikes_etl"
string = "datalake//distances-{}.csv".format(month_string)

sql_create_table = """CREATE TABLE IF NOT EXISTS {} (
ride_id TEXT PRIMARY KEY,
distance FLOAT
);
""".format(table_name)
# common data operations
data = pd.read_csv(string)


if con is not None:
        try:
            c = con.cursor()
            c.execute(sql_create_table)
            print("Created the table or checked it exists")
        except Exception as e:
            print(e)  
   
data.to_sql(name = table_name, con = con, if_exists='append', index = False)


    
