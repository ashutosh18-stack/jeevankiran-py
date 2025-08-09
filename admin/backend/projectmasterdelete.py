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

# Folder path
folder_path = f"projectuploads/{project_id}"

# Step 1: Recursively delete folder and contents
if os.path.exists(folder_path):
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))
    os.rmdir(folder_path)

# Safe and clean method
delete_package_query = "DELETE FROM packagemaster WHERE project_id = %s"
delete_project_query = "DELETE FROM projectmaster WHERE project_id = %s"

mycursor.execute(delete_package_query, (project_id,))
mycursor.execute(delete_project_query, (project_id,))
mydb.commit()



print(f'''<script>alert("Project Deleted successfully");
      location.href="../projectlist.py"</script> ''')
