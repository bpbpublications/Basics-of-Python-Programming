import mysql.connector
# Connect to the MySQL server
conn=mysql.connector.connect(
    host="localhost",   
    user="root",    
    password="sasml" 
)
# Create a database
dbname = "student"
sqlquery = f"CREATE DATABASE IF NOT EXISTS {dbname};"
cursor=conn.cursor()
cursor.execute(sqlquery)
# Switch to the new database
conn.database=dbname
# Define a SQL command to create a table
cursor.execute("""CREATE TABLE IF NOT EXISTS studenttbl
               (regid INT AUTO_INCREMENT PRIMARY KEY,first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,course VARCHAR(255),mobile INT)""")
conn.commit()
conn.close()
print("Database and table created successfully!")




    
