#!C:\Python312\python.exe
import cgi
import cgitb
import mysql.connector
import http.cookies
import os
import sys
cgitb.enable()
print("Content-Type: text/html\n")
cookie = http.cookies.SimpleCookie()
cookie.load(os.environ.get('HTTP_COOKIE', ''))
if "id" in cookie:
    user_id = cookie["id"].value
else:
    print("<h3 style='color:red;'>Unauthorized access. Please login first.</h3>")
    sys.exit()
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="jeevankiran"
    )
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM signup WHERE id = %s", (user_id,))
    user = cursor.fetchone()

    if not user:
        print("<h3 style='color:red;'>User not found!</h3>")
        sys.exit()

except Exception as e:
    print(f"<h3 style='color:red;'>Database error: {e}</h3>")
    sys.exit()
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Edit Profile</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container mt-5" style="max-width: 600px;">
  <h2 class="text-center mb-4">Edit Profile</h2>
  <form action="updatedprofile.py" method="POST" enctype="multipart/form-data">
    <input type="hidden" name="id" value="{user[0]}">

    <div class="mb-3">
      <label class="form-label">Full Name</label>
      <input type="text" class="form-control" name="fullname" value="{user[1]}" required>
    </div>

    <div class="mb-3">
      <label class="form-label">Email</label>
      <input type="email" class="form-control" name="email" value="{user[2]}" required>
    </div>

    <div class="mb-3">
      <label class="form-label">Phone Number</label>
      <input type="tel" class="form-control" name="phonenumber" value="{user[3]}" required>
    </div>

    <div class="mb-3">
      <label class="form-label">Date of Birth</label>
      <input type="date" class="form-control" name="DateofBirth" value="{user[4]}" required>
    </div>

    <div class="mb-3">
      <label class="form-label">Password</label>
      <input type="password" class="form-control" name="password" value="{user[5]}" required>
    </div>

    <div class="mb-3">
      <label class="form-label">Confirm Password</label>
      <input type="password" class="form-control" name="confirm_password" value="{user[5]}" required>
    </div>

    <div class="d-grid">
      <button type="submit" class="btn btn-warning rounded-pill">Update Profile</button>
    </div>
  </form>
</div>
</body>
</html>
""")
