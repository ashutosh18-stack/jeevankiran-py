#!C:/Python312/python.exe
import cgi
import cgitb
import os
import shutil
import mysql.connector

cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()

# Get form values
project_id = form.getvalue("project_id")
new_title = form.getvalue("title").strip()
description = form.getvalue("description")
status = form.getvalue("status")

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
cursor = mydb.cursor()

# Get old project data
cursor.execute(f"SELECT * FROM projectmaster WHERE project_id={project_id}")
old_data = cursor.fetchone()

old_img1 = old_data[4]
old_img2 = old_data[5]
old_img3 = old_data[6]

# ✅ Folder name is the project ID (not title)
folder_name = str(project_id)
upload_dir = os.path.join("projectuploads", folder_name)

# Create folder if doesn't exist
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)
def save_image(fileitem, index):
    if fileitem.filename:
        old_img_name = [old_img1, old_img2, old_img3][index]
        old_img_path = os.path.join(upload_dir, old_img_name)

        if os.path.isfile(old_img_path):
            try:
                os.remove(old_img_path)
            except PermissionError:
                print(f"<script>alert('Permission denied while removing: {old_img_path}'); window.history.back();</script>")
                exit()

        ext = os.path.splitext(fileitem.filename)[1]
        new_filename = f"{folder_name}_update_{index+1}{ext}"
        new_path = os.path.join(upload_dir, new_filename)

        with open(new_path, "wb") as f:
            f.write(fileitem.file.read())
        return new_filename
    else:
        return [old_img1, old_img2, old_img3][index]


# Handle images
img1 = save_image(form["image1"], 0)
img2 = save_image(form["image2"], 1)
img3 = save_image(form["image3"], 2)

# Update query
update_sql = f"""
    UPDATE projectmaster 
    SET project_title=%s, project_description=%s, status=%s, 
        project_img1=%s, project_img2=%s, project_img3=%s
    WHERE project_id=%s
"""
cursor.execute(update_sql, (new_title, description, status, img1, img2, img3, project_id))
mydb.commit()
mydb.close()

# Success response
print("<script>alert('Project updated successfully!');window.location.href='../projectlist.py';</script>")
