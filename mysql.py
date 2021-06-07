import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user = "arun",passwd = "1234",database="aj")

mycursor = mydb.cursor()

mycursor.execute("select * from student")

result = mycursor.fetchone()

for i in result:
	print(i)

