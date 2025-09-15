#!C:/Python312/python.exe
import cgi
import cgitb
import os
import shutil
import mysql.connector

cgitb.enable()
print("Content-Type:text/html\n")

form = cgi.FieldStorage()
id = form.getvalue("id")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
mycursor = mydb.cursor()

mycursor.execute(f'''DELETE FROM volunteer WHERE id = {id}''')
mydb.commit()

print('''
    <script>
        alert("Volunteer Deleted Successfully!");
        location.href = "../volunteerlist.py";
    </script>
''')
