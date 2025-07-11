#!C:/Python312/python.exe
import cgi
import os
import mysql.connector

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
name = form.getvalue("ngo_name")
ngo_email = form.getvalue("email")
ngo_phone = form.getvalue("phone")
ngo_description = form.getvalue("description")
ngo_address = form.getvalue("address")
ngo_facebook = form.getvalue("facebook")
ngo_twitter = form.getvalue("twitter")
ngo_instagram = form.getvalue("instagram")
file_item = form["logo"]

# Folder to save images
upload_dir = "ngomasteruploads"

# Make sure folder exists
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)

if file_item.filename:
    # Get file extension
    ext = os.path.splitext(file_item.filename)[1]
    image_filename = f"{name}{ext}"
    image_path = os.path.join(upload_dir, image_filename)

    # Save image file to folder
    with open(image_path, "wb") as f:
        f.write(file_item.file.read())

    # Insert data into MySQL using parameterized query
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="jeevankiran"
        )
        cursor = db.cursor()

        sql = f"INSERT INTO ngomaster (ngo_name, ngo_email, ngo_phone, ngo_logo , ngo_description, ngo_address , ngo_instagram ,ngo_twitter, ngo_facebook) VALUES ('{name}','{ngo_email}','{ngo_phone}','{image_filename}','{ngo_description}','{ngo_address}','{ngo_instagram}','{ngo_twitter}','{ngo_facebook}')"
        

        cursor.execute(sql)
        db.commit()
        # print(f"<h3>Upload successful! Image saved as: {image_filename}</h3>")
        print('''
      <script>alert("data added succesfully!");
      location.href="../ngomasterlist.py"</script>
      ''')
       

    except mysql.connector.Error as err:
        print(f"<h3>Database Error: {str(err)}</h3>")
    finally:
        cursor.close()
        db.close()
else:
    print("<h3>No file uploaded</h3>")
