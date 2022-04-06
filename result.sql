DROP VIEW IF EXISTS bikes_view;

CREATE VIEW bikes_view AS  
SELECT ride_id, started_at, ended_at, 
        ROUND(86400/60*(julianday(ended_at) - julianday(started_at)),2) as duration_minutes,
        strftime('%w', started_at) as weekeday
FROM bikes;

DROP VIEW IF EXISTS BI_view;

CREATE VIEW BI_view AS  
SELECT weekeday, ROUND(AVG(duration_minutes),1) as "Average_Duration" FROM bikes_view

GROUP BY weekeday;

/* Query to perform groupby and obtain final result */
SELECT weekeday, ROUND(AVG(duration_minutes),1) as "Average_Duration" FROM bikes_view

GROUP BY weekeday