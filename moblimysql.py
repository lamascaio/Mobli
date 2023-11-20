import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='mobli' 
)
cursor = conexao.cursor()



cursor.close()
conexao.close()