#!C:/Python312/python.exe

import cgi
import cgitb
import os
import mysql.connector

cgitb.enable()
print("Content-Type: text/html\n")

# Get project_id from form
form = cgi.FieldStorage()
project_id = form.getvalue("project_id")

# Connect to database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
mycursor = mydb.cursor()



# Safe and clean method
delete_package_query = "DELETE FROM packagemaster WHERE project_id = %s"
delete_project_query = "DELETE FROM projectmaster WHERE project_id = %s"

mycursor.execute(delete_package_query, (project_id,))
mycursor.execute(delete_project_query, (project_id,))
mydb.commit()



print(f'''<script>alert("Project Deleted successfully");
      location.href="../projectlist.py"</script> ''')
