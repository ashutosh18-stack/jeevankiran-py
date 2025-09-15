#!C:/Python312/python.exe
import cgi
import os
import mysql.connector
import cgitb
cgitb.enable()

print("Content-Type: text/html\n")

form = cgi.FieldStorage()

# Get form values
package_id = form.getvalue('id')
project_id = form.getvalue('project')
item = form.getvalue('item').strip()
package_qty = form.getvalue('qty')
package_price = form.getvalue('price')
package_description = form.getvalue('description')
package_status = form.getvalue('status')
image_field = form['image1'] if 'image1' in form else None

# DB connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
mycursor = mydb.cursor(dictionary=True)

# Get old image name
mycursor.execute("SELECT package_img FROM packagemaster WHERE package_id = %s", (package_id,))
old_data = mycursor.fetchone()
old_img = old_data['package_img'] if old_data else ""

# Set upload directory
upload_dir = os.path.join("packageuploads", str(package_id))
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)

def save_image(fileitem):
    if fileitem is not None and fileitem.filename:
        # Remove old image
        old_img_path = os.path.join(upload_dir, old_img)
        if os.path.isfile(old_img_path):
            try:
                os.remove(old_img_path)
            except PermissionError:
                print(f"<script>alert('Permission denied while removing old image.'); window.history.back();</script>")
                exit()

        # Save new image
        ext = os.path.splitext(fileitem.filename)[1]
        new_filename = f"{package_id}_updated{ext}"
        new_path = os.path.join(upload_dir, new_filename)
        with open(new_path, "wb") as f:
            f.write(fileitem.file.read())
        return new_filename
    return old_img

new_img = save_image(image_field)

# Update database
update_sql = f"""
    UPDATE packagemaster 
    SET package_item = '{item}', project_id = '{project_id}', package_qty = '{package_qty}', package_price = '{package_price}', 
        package_description = '{package_description}', package_img = '{new_img}', package_status = '{package_status}'
    WHERE package_id = '{package_id}'
"""
mycursor.execute(update_sql)
mydb.commit()

print("<script>alert('Package updated successfully'); location.href='../packagelist.py';</script>")
