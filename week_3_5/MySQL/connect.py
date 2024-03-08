import mysql.connector

# Credentials
MYSQL_USER="longvu" 
MYSQL_PASSWORD='10122002'
MYSQL_SERVER="127.0.0.1" 
#MYSQL_PORT=3306
MYSQL_DB="db_01"

# connect
conn = mysql.connector.connect(
  
  host = MYSQL_SERVER,
  database = MYSQL_DB,
  user = MYSQL_USER,
  password = MYSQL_PASSWORD

)

# Cursor:
cursor = conn.cursor()

# Query: 
query = "SELECT * FROM var_squad"
cursor.execute(query)

# Fetch
rows = cursor.fetchall()
for row in rows:
  print (row)




result = cursor.fetchall()
# Close session
conn.commit()
cursor.close()
conn.close()



