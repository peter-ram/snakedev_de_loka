
month_string := "202202" 
default: scraper unzipper sqlite-ops-raw etl-step sqlite-ops-etl

argument-test:
  echo test_arg

scraper:
  python3 scraper.py {{month_string}}

# unzipping file
unzipper:
  python3 unzipper.py {{month_string}}

#loading raw data to DB step
sqlite-ops-raw:
  python3 sqlite_raw.py {{month_string}}

#etl step - compute distances
etl-step:
  python3 compute_distances_etl.py {{month_string}}

sqlite-ops-etl:
  python3 sqlite_etl.py {{month_string}}