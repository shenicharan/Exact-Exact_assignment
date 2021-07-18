--Create statement for the table to load the data
CREATE TABLE "YELLOW_TAXI_DATA" (
"VendorID" INTEGER,
  "tpep_pickup_datetime" datetime,
  "tpep_dropoff_datetime" datetime,
  "passenger_count" INTEGER,
  "trip_distance" REAL,
  "RatecodeID" INTEGER,
  "store_and_fwd_flag" TEXT,
  "PULocationID" INTEGER,
  "DOLocationID" INTEGER,
  "payment_type" INTEGER,
  "fare_amount" REAL,
  "extra" REAL,
  "mta_tax" REAL,
  "tip_amount" REAL,
  "tolls_amount" REAL,
  "improvement_surcharge" REAL,
  "total_amount" REAL,
  "congestion_surcharge" REAL,
  "tip_percent" REAL,
  "quarter" INTEGER,
  "trip_duration" REAL,
  "trip_duration" REAL,
  "speed" REAL
)

-- To find location of maximum of tip in comparison to totoal amount for every quarter
select max(tip_percent),DOLocationID,quarter from yellow_taxi_data

-- To find location of maximum of tip in comparison to totoal amount for every quarter
select max(speed),trip_hour,tpep_dropoff_datetime from yellow_taxi_data group by trip_hour,tpep_dropoff_datetime