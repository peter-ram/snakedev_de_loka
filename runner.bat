set month= "202112" 

:: caling scraper: note that only files with prefix JC will be used
python scraper.py %month%

:: unzipping file
python unzipper.py %month%

:: loading raw data to DB step
python sqlite_ops.py %month% raw_loader

:: ETL step working
python compute_distances_etl.py %month%


:: loading etl processed data to DB table
python sqlite_ops.py %month% etl_loader


