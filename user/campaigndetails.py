#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
import mysql.connector
import header

form = cgi.FieldStorage()
project_id = form.getvalue('project_id')

user_id = form.getvalue("id")
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)

cursor = mydb.cursor(dictionary=True)

# Fetch project details
cursor.execute(f"SELECT * FROM projectmaster WHERE project_id = '{project_id}'")
project = cursor.fetchone()
status = project['status']

project_title = project['project_title']
id = project['project_id']
image = project['project_img2']
image2 = project['project_img3']
image_path = f''' ../admin/backend/projectuploads/{id}/{image}'''
image_path2 = f''' ../admin/backend/projectuploads/{id}/{image2}'''

# Fetch packages
mycursor = mydb.cursor(dictionary=True)
mycursor.execute("SELECT * FROM packagemaster WHERE project_id = %s", (project_id,))
packages = mycursor.fetchall()

# Start HTML
print('''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Project Details</title>
  <link rel="stylesheet" href="css/bootstrap.min.css">
  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

 <style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  html, body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f5f5f5;
    color: #333;
    overflow-x: hidden; /* Prevent horizontal scroll */
  }

  .hero-wrap {
    position: relative;
    width: 100%;
    height: 250px;
    overflow: hidden;
  }

  .overlay-text {
    position: absolute;
    top: 100px;
    width: 100%;
    background: rgba(0, 0, 0, 0.5);
    color: white;
    padding: 20px 10px;
    text-align: center;
    font-size: 2rem;
    font-weight: bold;
    z-index: 2;
    border-bottom: 2px solid orange;
    text-transform: uppercase;
  }

  .project-card {
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    overflow: hidden;
    transition: 0.3s;
    background-color: #fff;
    position: relative;
  }

  .project-card:hover {
    transform: translateY(-5px);
  }

  .project-img {
    width: 100%;
    height: 200px;
    object-fit: cover;
  }

  .package-status-label {
    position: absolute;
    top: 10px;
    left: 10px;
    background-color: orange;
    padding: 5px 10px;
    font-size: 12px;
    font-weight: bold;
    color: white;
    border-radius: 5px;
    z-index: 2;
    text-transform: uppercase;
  }

  .truncate-description {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
    min-height: 4.5em;
    white-space: normal;
    word-wrap: break-word;
  }

  .disabled-overlay {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: rgba(0, 0, 0, 0.7);
    z-index: 9999;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 24px;
    font-weight: bold;
    text-align: center;
  }

  /* Slider Background Fix */
  .slider {
    display: flex;
    width: 200%;
    height: 100%;
    animation: slideLeft 20s linear infinite;
    overflow: hidden;
  }

  .slide {
    flex: 0 0 50%;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
  }

  @keyframes slideLeft {
    0% { transform: translateX(0%); }
    100% { transform: translateX(-50%); }
  }
</style>
''')
print(f'''
</head>
<body>

<!-- Hero Section -->
<div class="hero-wrap" style="background-image: url('images/bg_1.jpg');">
  <div class="overlay-text"><span>{project_title}</span></div>
</div>

<!-- Package Cards -->
<section class="ftco-section py-5">
  <div class="container">
    <div class="row">
''')

# Loop through packages
for pack in packages:
    package_id = pack['package_id']
    package_item = pack['package_item']
    package_description = pack['package_description']
    package_img = pack['package_img']
    package_status = pack['package_status']
    package_qty = pack['package_qty']
    package_price = pack['package_price']
    img_path = f"../admin/backend/packageuploads/{package_id}/{package_img}"

    print(f'''
    <div class="col-md-3 mb-4">
     <a href="projectdonor.py?id={user_id}&package_id={package_id}" style="text-decoration: none; color: inherit;">
      <div class="project-card text-center p-3">
        <div class="package-status-label">{package_status}</div>
        <img src="{img_path}" alt="Package Image" class="project-img mb-3">
        <h5>{package_item}</h5>
        <p class="truncate-description">{package_description}</p>
        <p><strong>Required Qty:</strong> {package_qty}</p>
        <p><strong>Required Amount:</strong> Rs:{package_price}</p>
        <span class="btn btn-primary">Donate</span>
      </div>
     </a>
    </div>
''')

print('''
    </div>
  </div>
</section>
''')

# Background slider
print(f'''
<div class="hero-wrap">
  <div class="slider" style="display: flex; width: 200%; height: 100vh; animation: slideLeft 20s linear infinite;">
    <div class="slide" style="flex: 0 0 50%; background-image: url('{image_path}'); background-size: cover;"></div>
    <div class="slide" style="flex: 0 0 50%; background-image: url('{image_path2}'); background-size: cover;"></div>
  </div>
  <div class="overlay-text"><span>{project_title}</span></div>
</div>
''')

# Overlay if project is completed
if status.lower() == 'completed':
    print('''
    <div class="disabled-overlay" id="disabledOverlay">
      This project is completed. You cannot interact with this page.
    </div>
    <script>
      document.body.style.pointerEvents = 'none';
      document.getElementById('disabledOverlay').style.pointerEvents = 'auto';
    </script>
    ''')

# Scripts and closing HTML
print('''
<script src="js/jquery.min.js"></script>
<script src="js/bootstrap.min.js"></script>
</body>
</html>
''')

import footer
