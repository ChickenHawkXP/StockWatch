import mysql.connector
import json

walmart_cols = list()
intel_cols = list()
nvidia_cols = list()
microsoft_cols = list()

with open("config.json","r") as json_read:
    data = json.load(json_read)
try:
    database = mysql.connector.connect(host = data['host'],
                                        user = data['user'],
                                        password = data['password'],
                                        database = data['database'],
                                        auth_plugin = data['auth_plugin'])
except:
    print('Could not make connection with database!')
cursor = database.cursor()
class getCols:
    def walmart():
        cursor.execute('DESCRIBE walmart;')
        for i in cursor:
            walmart_cols.append(i[0])
        return walmart_cols
    def intel():
        cursor.execute('DESCRIBE intel;')
        for i in cursor:
            intel_cols.append(i[0])
        return intel_cols
    def nvidia():
        cursor.execute('DESCRIBE nvidia;')
        for i in cursor:
            nvidia_cols.append(i[0])
        return nvidia_cols
    def microsoft():
        cursor.execute('DESCRIBE microsoft;')
        for i in cursor:
            microsoft_cols.append(i[0])
        return microsoft_cols

def addData(db,price,pe,div):
    cursor.execute('''INSERT INTO %s VALUES(%d,%s,%s)''' %(db,price,pe,div))
    database.commit()
    

  
