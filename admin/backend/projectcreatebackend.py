#!C:/Python312/python.exe
import cgi
import cgitb
import os
import mysql.connector

cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
title = form.getvalue("title")
description = form.getvalue("description")
status = form.getvalue("status")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
mycursor = mydb.cursor()

insert_sql = """
    INSERT INTO projectmaster (project_title, project_description, status)
    VALUES (%s, %s, %s)
"""
mycursor.execute(insert_sql, (title, description, status))
mydb.commit()
project_id = mycursor.lastrowid

base_dir = "projectuploads"
project_folder_path = os.path.join(base_dir, str(project_id))

if not os.path.exists(project_folder_path):
    os.makedirs(project_folder_path)

image_fields = ["image1", "image2", "image3"]
saved_image_names = []

for index, field_name in enumerate(image_fields, start=1):
    file_item = form[field_name]
    if file_item.filename:
        ext = os.path.splitext(file_item.filename)[1]
        image_name = f"{title.replace(' ', '_')}_{index}{ext}"
        image_path = os.path.join(project_folder_path, image_name)

        with open(image_path, 'wb') as f:
            f.write(file_item.file.read())

        saved_image_names.append(image_name)
    else:
        saved_image_names.append("")

update_sql = """
    UPDATE projectmaster
    SET project_img1 = %s, project_img2 = %s, project_img3 = %s
    WHERE project_id = %s
"""
mycursor.execute(update_sql, (*saved_image_names, project_id))
mydb.commit()

print('''
<script>
    alert("Project added successfully");
    location.href="../projectlist.py";
</script>
''')
