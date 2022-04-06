
month_string := "202202" 
default: scraper unzipper sqlite_ops_raw average_trip_duration compute_distances_step sqlite_ops_compute_distances

argument_test:
  echo test_arg

scraper:
  python3 scraper.py {{month_string}}

# unzipping file
unzipper:
  python3 unzipper.py {{month_string}}

#loading raw data to DB step
sqlite_ops_raw:
  python3 sqlite_raw.py {{month_string}}

# step to create the view and execute query script to get result
average_trip_duration:
  sqlite3 bikes-warehouse.db -init result.sql 
#etl step - compute distances
compute_distances_step:
  python3 compute_distances.py {{month_string}}

sqlite_ops_compute_distances:
  python3 sqlite_compute_distances.py {{month_string}}