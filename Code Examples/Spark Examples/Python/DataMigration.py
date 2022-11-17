  #Query Script: CREATE TABLE  	rdddata( ID INT, VALUE TEXT); CHANged!!!
from pyspark import SparkContext
sc = SparkContext(appName='SparkWordCount Example')
print("Context", sc)
inputFile = sc.textFile('C:\\InputFile.txt')
print(inputFile)
counts = inputFile.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
# Console Output
rdd2Text=counts
print("Counted:",rdd2Text )

#Wrting file
fileOb=open("D:\\Results.txt","w")
fileOb.write("RDD Datasets" + str(rdd2Text))

#Wrting to database
import mysql.connector
dbCon = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='cdpdb')
print("Connection Object:", dbCon)
cursorObj=dbCon.cursor()
sqlQueryRDD="INSERT INTO RDDData(ID, VALUE) VALUES(101,'"+ str(rdd2Text)+"')"
print("Query",sqlQueryRDD)
cursorObj.execute(sqlQueryRDD)
dbCon.commit()
dbCon.close()
#Writing to HDFS
sc.stop()

#Reading from NoSQL Database

