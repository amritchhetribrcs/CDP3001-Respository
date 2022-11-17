from pyspark import SparkContext
sc = SparkContext(appName='SparkWordCount Example')
print("Context", sc)
inputFile = sc.textFile('C:\\InputFile.txt')
print(inputFile)
counts = inputFile.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
# Console Output
rdd2Text=counts
print("Counted:",rdd2Text )
