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

# Insert campaign
insert_sql = """
    INSERT INTO campaignmaster (title, description, status)
    VALUES (%s, %s, %s)
"""
mycursor.execute(insert_sql, (title, description, status))
mydb.commit()
id = mycursor.lastrowid

# Create folder
base_dir = "campaignuploads"
campaign_folder_path = os.path.join(base_dir, str(id))
if not os.path.exists(campaign_folder_path):
    os.makedirs(campaign_folder_path)

# Save images
image_fields = ["image1", "image2", "image3"]
saved_image_names = []

for index, field_name in enumerate(image_fields, start=1):
    if field_name in form:
        file_item = form[field_name]
        if file_item.filename:
            ext = os.path.splitext(file_item.filename)[1]
            image_name = f"{title.replace(' ', '_')}_{index}{ext}"
            image_path = os.path.join(campaign_folder_path, image_name)

            with open(image_path, 'wb') as f:
                f.write(file_item.file.read())

            saved_image_names.append(image_name)
        else:
            saved_image_names.append("")
    else:
        saved_image_names.append("")

# Update with image names
update_sql = """
    UPDATE campaignmaster
    SET img1 = %s, img2 = %s, img3 = %s
    WHERE id = %s
"""
mycursor.execute(update_sql, (*saved_image_names, id))
mydb.commit()

print('''
<script>
    alert("Campaign added successfully");
    location.href="../Campaignlist.py";
</script>
''')






  