#!C:/Python312/python.exe
import cgi
import cgitb
import os
import shutil
import mysql.connector

cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()

id = form.getvalue("id")
name = form.getvalue("name")
email = form.getvalue("email")
message = form.getvalue("message")


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
cursor = mydb.cursor()


cursor.execute(f"SELECT * FROM volunteer WHERE id={id}")
old_data = cursor.fetchone()


update_sql = f"""
    UPDATE volunteer
    SET name='{name}', email='{email}', message='{message}'
    WHERE id='{id}'
"""
cursor.execute(update_sql)
mydb.commit()
mydb.close()

print("<script>alert('volunteer updated successfully!');window.location.href='../volunteerlist.py';</script>")
