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
cursor.execute("""UPDATE studenttbl SET first_name = 'Ajay',
                last_name='Singh',course='Java',mobile='1234567890'
                where regid = 32""")
# fetch all the records in a table using fetchall() 
display = cursor.fetchall()
conn.commit()
cursor.execute("""SELECT * FROM studenttbl 
                where regid = 32""")
display = cursor.fetchall()
# fetch the records using loops and display using '\n'
for x in display:
    print(x,'\n')
# Changes are commit to the database
conn.commit()
# Close the cursor and connection
cursor.close()
conn.close()



