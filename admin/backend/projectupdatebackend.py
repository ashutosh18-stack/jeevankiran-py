#!C:/Python312/python.exe
import cgi
import cgitb
import os
import shutil
import mysql.connector

cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()

project_id = form.getvalue("project_id")
new_title = form.getvalue("title").strip()
description = form.getvalue("description")
status = form.getvalue("status")


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
cursor = mydb.cursor()


cursor.execute(f"SELECT * FROM projectmaster WHERE project_id={project_id}")
old_data = cursor.fetchone()

old_title = old_data[1]
old_img1 = old_data[4]
old_img2 = old_data[5]
old_img3 = old_data[6]

old_folder = old_title.replace(" ", "_")
new_folder = new_title.replace(" ", "_")

upload_dir = os.path.join("projectuploads", new_folder)

old_folder_path = os.path.join("projectuploads", old_folder)
if old_folder != new_folder:
    if os.path.exists(old_folder_path):
        os.rename(old_folder_path, upload_dir)
else:
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)


def save_image(fileitem, index):
    if fileitem.filename:

        old_img_name = [old_img1, old_img2, old_img3][index]
        old_img_path = os.path.join(upload_dir, old_img_name)
        if os.path.exists(old_img_path):
            os.remove(old_img_path)


        ext = os.path.splitext(fileitem.filename)[1]
        new_filename = f"{new_folder}_update_{index+1}{ext}"
        new_path = os.path.join(upload_dir, new_filename)

        with open(new_path, "wb") as f:
            f.write(fileitem.file.read())
        return new_filename
    else:
        return [old_img1, old_img2, old_img3][index]

img1 = save_image(form["image1"], 0)
img2 = save_image(form["image2"], 1)
img3 = save_image(form["image3"], 2)

update_sql = f"""
    UPDATE projectmaster 
    SET project_title='{new_title}', project_description='{description}', status='{status}', 
        project_img1='{img1}', project_img2='{img2}', project_img3='{img3}'
    WHERE project_id='{project_id}'
"""
cursor.execute(update_sql)
mydb.commit()
mydb.close()

print("<script>alert('Project updated successfully!');window.location.href='../projectlist.py';</script>")
