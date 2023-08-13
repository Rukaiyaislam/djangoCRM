#Install Mysql on your computer
#https://dev.mysql.com/downloads/installer/
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python
#Out-File -FilePath mydb.py -Force

#coding: utf-8

import mysql.connector
 
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'W@2915djkq#'
) 

# prepare a cursor object
cursorObject = dataBase.cursor()

#Create a database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")