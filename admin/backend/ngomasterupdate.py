#!C:/Python312/python.exe
import cgi
import os
import mysql.connector
import cgitb
cgitb.enable()

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
ngo_id = form.getvalue("ngo_id")
ngo_name = form.getvalue("edit_ngo_name")
email = form.getvalue("edit_email")
phone = form.getvalue("edit_phone")
description = form.getvalue("edit_description")
address = form.getvalue("edit_address")
instagram = form.getvalue("edit_instagram")
twitter = form.getvalue("edit_twitter")
facebook = form.getvalue("edit_facebook")
file_item = form["edit_logo"] if "edit_logo" in form else None

upload_dir = "ngomasteruploads"
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
cursor = db.cursor()

cursor.execute(f"SELECT ngo_logo FROM ngomaster WHERE ngo_id = '{ngo_id}'")
result = cursor.fetchone()
old_logo = result[0] if result else ""
new_logo_filename = old_logo
ext = os.path.splitext(old_logo)[1] if old_logo else ""

if "edit_logo" in form and form["edit_logo"].filename:
    file_item = form["edit_logo"]

    old_path = os.path.join(upload_dir, old_logo)
    if os.path.exists(old_path):
        os.remove(old_path)

    ext = os.path.splitext(file_item.filename)[1]
    new_logo_filename = f"{ngo_name.strip().replace(' ', '_')}{ext}"
    new_path = os.path.join(upload_dir, new_logo_filename)

    with open(new_path, "wb") as f:
        f.write(file_item.file.read())

else:
    if old_logo:
        old_path = os.path.join(upload_dir, old_logo)
        new_logo_filename = f"{ngo_name.strip().replace(' ', '_')}{ext}"
        new_path = os.path.join(upload_dir, new_logo_filename)

        if old_logo != new_logo_filename and os.path.exists(old_path):
            os.rename(old_path, new_path)

update_sql = f"""
    UPDATE ngomaster SET
        ngo_name = '{ngo_name}',
        ngo_email = '{email}',
        ngo_phone = '{phone}',
        ngo_logo = '{new_logo_filename}',
        ngo_description = '{description}',
        ngo_address = '{address}',
        ngo_instagram = '{instagram}',
        ngo_twitter = '{twitter}',
        ngo_facebook = '{facebook}'
    WHERE ngo_id = {ngo_id}
"""
cursor.execute(update_sql)
db.commit()
cursor.close()
db.close()
print("""
<script>
    alert("NGO updated successfully!");
    location.href = "../ngomasterlist.py";
</script>
""")
