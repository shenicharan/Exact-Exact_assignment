# Exact-Exact_assignment
There are 4 steps in the assignment solution.
1. ETL_Yellow_Taxi_Data.HTML : This file contains the steps for ETL process written in PYSPARK using Databricks community edition. Data is extracted and stored in databricks local file location. Finally , data is saved as parquet files. Also it is loaded into SQL database for further processing.
2. Final_query.sql file conatins the SQL statement for the insight required from data. These statements can be executed on top of data loaded in SQL database.
3. app.py is python file having logic written for creating REST API end points for insights to be available for user. It is written using flask by consuming the data present in SQL database.
4. project_architecture file is having pictorial diagram of the solution.

PS: Extraction and transformation logic is complete but data could not loaded in the SQLITE database due to limitation in databricks community edition. 
