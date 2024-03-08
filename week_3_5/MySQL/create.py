import mysql.connector

# Credentials
MYSQL_USER = "longvu" 
MYSQL_PASSWORD = '10122002'
MYSQL_SERVER = "127.0.0.1" 
MYSQL_DB = "db_01"

conn = mysql.connector.connect(
    host=MYSQL_SERVER,
    database=MYSQL_DB,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD
)

cursor = conn.cursor()

# Query: 
query = '''
    INSERT INTO var_squad (name, alias) 
    VALUES ( 'CMH', 'wolf'),
           ( 'MOC', 'prince'),
           ( 'XS', 'shower')
'''
cursor.execute(query)
print(query)

# Commit (local to server)
conn.commit()

# Close session
cursor.close()
conn.close()