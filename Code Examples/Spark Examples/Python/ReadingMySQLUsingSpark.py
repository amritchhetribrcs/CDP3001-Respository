#Query Script: CREATE TABLE  	rdddata( ID INT, VALUE TEXT);
import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("SQL Tables")\
    .config("spark.executor.extraClassPath","C:\BigData-Analytics\Driver-Software-Jars\mysql-connector-j-8.0.31\mysql-connector-j-8.0.31.jar")\
    .config("spark.driver.extraClassPath","C:\BigData-Analytics\Driver-Software-Jars\mysql-connector-j-8.0.31\mysql-connector-j-8.0.31.jar")\
    .getOrCreate()
print("Contex", spark)
url = "jdbc:mysql://localhost:3306/cdpdb"
driver = "com.mysql.jdbc.Driver"
user = "root"
password = ""
df =  spark.read\
    .format("jdbc")\
    .option("driver", driver)\
    .option("url", url)\
    .option("user", user)\
    .option("password", password)\
    .option("dbtable", "RDDData")\
    .load()
print("MySQL Data Frame", df)
print(" Column Count",df.count())

sqlQuery="( SELECT * FROM rdddata WHERE 1) as RDDTable"
df =  spark.read\
    .format("jdbc")\
    .option("driver", driver)\
    .option("url", url)\
    .option("user", user)\
    .option("password", password)\
    .option("dbtable", sqlQuery)\
    .load()
df.show(3)



