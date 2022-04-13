
month_string := "202202" 
default: scraper unzipper sqlite_ops_raw average_trip_duration compute_distances_step sqlite_ops_compute_distances data_quality


scraper:
  python3 scraper.py {{month_string}}

# unzipping file
unzipper: scraper
  python3 unzipper.py {{month_string}}

#loading raw data to DB step
sqlite_ops_raw: unzipper
  python3 sqlite_raw.py {{month_string}}

# step to create the view and execute query script to get result
average_trip_duration: sqlite_ops_raw
  sqlite3 bikes-warehouse.db -init result.sql .exit
  


compute_distances_step: average_trip_duration
  python3 compute_distances.py {{month_string}}

# uploading distances to new table with that specific logic
sqlite_ops_compute_distances: compute_distances_step
  python3 sqlite_compute_distances.py {{month_string}}
  

# data integrity check
data_quality: 
  python3 data_quality.py {{month_string}}