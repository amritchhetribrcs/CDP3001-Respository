import mysql.connector
dbCon = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='cdpdb')
print("Connection Object:", dbCon)
cursorObj=dbCon.cursor()
cursorObj.execute("INSERT INTO RDDData(ID, VALUE) VALUES(100, 'RDDSDATA-1')")
dbCon.commit()
dbCon.close()
