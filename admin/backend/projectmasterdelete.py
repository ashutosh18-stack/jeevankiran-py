#!C:/Python312/python.exe
import cgi
import cgitb
import os
import shutil
import mysql.connector

cgitb.enable()
print("Content-Type:text/html\n")

form = cgi.FieldStorage()
project_id = form.getvalue("project_id")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT project_title FROM projectmaster WHERE project_id = %s", (project_id,))
row = mycursor.fetchone()

project_title = row[0]
folder_name = project_title.replace(" ", "_")
folder_path = os.path.join("projectuploads", folder_name)

shutil.rmtree(folder_path)

mycursor.execute(f"DELETE FROM projectmaster WHERE project_id = {project_id}")
mydb.commit()

print('''
    <script>
        alert("Project Deleted Successfully!");
        location.href = "../projectlist.py";
    </script>
''')
