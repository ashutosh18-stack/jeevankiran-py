#!C:/Python312/python.exe
import cgi
import cgitb
import os
import mysql.connector
import shutil

cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
title = form.getvalue("title")
description = form.getvalue("description")
status = form.getvalue("status")

base_dir = "projectuploads"
project_folder_name = title.replace(" ", "_")
project_folder_path = os.path.join(base_dir, project_folder_name)

if not os.path.exists(project_folder_path):
    os.makedirs(project_folder_path)

image_fields = ["image1", "image2", "image3"]
saved_image_names = []

for index, field_name in enumerate(image_fields, start=1):
    file_item = form[field_name]
    if file_item.filename:
        ext = os.path.splitext(file_item.filename)[1]
        image_name = f"{project_folder_name}_{index}{ext}"
        image_path = os.path.join(project_folder_path, image_name)

        with open(image_path, 'wb') as f:
            f.write(file_item.file.read())

        saved_image_names.append(image_name)
    else:
        saved_image_names.append("")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)

mycursor = mydb.cursor()

sql = """
    INSERT INTO projectmaster (
        project_title, project_description, status, 
        project_img1, project_img2, project_img3
    ) VALUES (%s, %s, %s, %s, %s, %s)
"""

values = (title, description, status, *saved_image_names)
mycursor.execute(sql, values)
mydb.commit()

print('''
<script> alert("project added successufully")
      location.href="../projectlist.py"</script>''')
