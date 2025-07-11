#!C:\Python312\python.exe

import cgi, os, mysql.connector
from datetime import datetime

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
ngo_name = form.getvalue("ngo_name")
logo = form["logo"]

# Save uploaded image
if logo.filename:
    upload_dir = "ngomasteruploads"  # change as per your server
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    
    filename = datetime.now().strftime("%Y%m%d%H%M%S_") + os.path.basename(logo.filename)
    filepath = os.path.join(upload_dir, filename)

    with open(filepath, 'wb') as f:
        f.write(logo.file.read())

    image_path = f"uploads/{filename}"  # Relative path to store in DB

    # Save to database
    conn = mysql.connector.connect(
        host="localhost", user="root", password="", database="jeevankiran"
    )
    cur = conn.cursor()
    cur.execute(f"INSERT INTO ngo (ngo_name, ngo_logo) VALUES ('{ngo_name}','{image_path}')", (ngo_name, image_path))
    conn.commit()
    conn.close()

    print("<h3>Upload successful!</h3>")
    print(f"<p>Saved as: {image_path}</p>")
else:
    print("<h3>Error: No file uploaded</h3>")
