default: scraper unzipper sqlite-ops-raw etl-step sqlite-ops-etl


scraper:
  python3 scraper.py "202202"

# unzipping file
unzipper:
  python3 unzipper.py "202202"

#loading raw data to DB step
sqlite-ops-raw:
  python3 sqlite_ops.py "202202" raw_loader

#etl step - compute distances
etl-step:
  python3 compute_distances_etl.py "202202"

sqlite-ops-etl:
  python3 sqlite_ops.py "202202" etl_loader