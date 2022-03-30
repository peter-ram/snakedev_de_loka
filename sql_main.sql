/* Initial Query for Table initialization */
CREATE TABLE IF NOT EXISTS bikes (
    ride_id integer PRIMARY KEY,
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
    period TEXT,
);

/* Intial Query for ETL table initialization */
CREATE TABLE IF NOT EXISTS bikes_etl (
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
    distance FLOAT
);

/* Query to Create View - good practice to have a view before analytics layer */
DROP VIEW IF EXISTS bikes_view;

CREATE VIEW bikes_view AS  
SELECT ride_id, started_at, ended_at, 
        ROUND(86400/60*(julianday(ended_at) - julianday(started_at)),2) as duration_minutes,
        strftime('%w', started_at) as weekeday
FROM bikes;


/* Query to perform groupby and obtain final result */
SELECT weekeday, ROUND(AVG(duration_minutes),1) as "Average_Duration" FROM bikes_view

GROUP BY weekeday