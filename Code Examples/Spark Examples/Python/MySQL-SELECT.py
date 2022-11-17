import mysql.connector
dbCon = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='cdpdb')
print("Connection Object:", dbCon)
cursorObj=dbCon.cursor()
cursorObj.execute("SELECT * FROM rdddata")
print("Result:", resultSet )
#dbCon.commit()
dbCon.close()
