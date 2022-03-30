import sqlite3
import pandas as pd
import sys

month_string = sys.argv[1]


con = sqlite3.connect('bikes-warehouse.db')


table_name = "bikes"
string = "datalake//JC-" + month_string + "-citibike-tripdata.csv"

sql_create_table = """CREATE TABLE IF NOT EXISTS {} (
ride_id TEXT PRIMARY KEY,
rideable_type TEXT,
started_at  DATETIME,
ended_at DATETIME,
start_station_name TEXT,
start_station_id TEXT,
end_station_name TEXT,
end_station_id TEXT,
start_lat FLOAT,
start_lng FLOAT,
end_lat FLOAT,
end_lng FLOAT,
member_casual TEXT,
period TEXT
);
""".format(table_name)
# common data operations
data = pd.read_csv(string)
data["period"] = month_string


if con is not None:
        try:
            c = con.cursor()
            c.execute(sql_create_table)
            print("Created the table or checked it exists")
        except Exception as e:
            print(e)  
   

data.to_sql(name = table_name, con = con, if_exists='append', index = False)


    
    
