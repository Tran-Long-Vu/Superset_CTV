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


# Get the last row
get_last_row_query = "SELECT * FROM var_squad ORDER BY id DESC LIMIT 1"
cursor.execute(get_last_row_query)
last_row = cursor.fetchone()

# Delete the last row
delete_last_row_query = "DELETE FROM var_squad WHERE id = %s"
cursor.execute(delete_last_row_query, (last_row[0],))
conn.commit()

# Print the deleted row
print("Deleted row:")
print(last_row)



result = cursor.fetchall()
# Close session
conn.commit()
cursor.close()
conn.close()



