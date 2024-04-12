import mysql.connector
# MySQL Database Connection Configuration
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="sasml",
    database="student"
)
# Cursor object and Connection interaction
cursor = conn.cursor()
# Executing SQL Query to insert a record into table 'studenttbl'
cursor.execute("""INSERT INTO studenttbl(regid,first_name,last_name,course,mobile) 
   VALUES(33,'Vijay','Kumar','Python',1234557791)""")
# Changes are commit to the database
conn.commit()
# Close the cursor and connection
cursor.close()
conn.close()
print("Record inserted successfully.")







