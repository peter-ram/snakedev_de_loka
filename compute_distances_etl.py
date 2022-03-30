import pandas as pd

import sqlite3
import pandas as pd
from haversine import haversine, Unit
import sys

# turn into script input
#month_string = "202202"
month_string = sys.argv[1]

print(month_string)

################# helper function ##################
# this helper functions simulates any ETL logic you may have

def distance_calculator(start_lat, start_lon, end_lat, end_lon):
    results = []
    for row in zip(start_lat, start_lon, end_lat, end_lon):
        start = (row[0], row[1])
        end = (row[2], row[3])
        results.append(haversine(start, end, unit = 'km'))
    return results


database = 'bikes-warehouse.db'

conn = sqlite3.connect(database)

# loading dataset
df = pd.read_sql("SELECT * from bikes WHERE period = {}".format(month_string), con=conn)
#computing great circle distance
df['distance'] = distance_calculator(df['start_lat'],df['start_lng'],df['end_lat'],df['end_lng'])

df.to_csv("datalake//distances-{}.csv".format(month_string), index = False)

conn.close()

print("Executed successfully")

