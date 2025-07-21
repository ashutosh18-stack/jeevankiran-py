#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
import header
import mysql.connector
import os
form = cgi.FieldStorage()
#print(form)
id = form.getvalue("id")
#print(id)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
mycursor = mydb.cursor()
query = f"SELECT * FROM volunteer WHERE id={id}"
#print(query)
mycursor.execute(query)
myresult = mycursor.fetchone()

name = myresult[1]
email = myresult[2]
message = myresult[3]

print(f''' 
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Edit Project</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
  <link rel="stylesheet" href="style/projectedit.css">
</head>
<body>

  <div class="wrapper">
    <div class="page-heading">
      <i class="fas fa-building"></i> Edit Volunteer
    </div>

    <form class="form-container" id="volunteerform" action="backend/volunteerupdatebackend.py" method="post" enctype="multipart/form-data">
    

      <!-- Project Title -->
         <div class="form-group">
        <label for="title">Id</label>
        <input type="text" id="id"  name="id" value="{id}" readonly>
      </div>
      <div class="form-group">
        <label for="title">Name</label>
        <input type="text" id="name" name="name" value="{name}" required>
      </div>

      <!-- Description -->
      <div class="form-group">
        <label for="description">Email</label>
        <input type="text" id="email" name="email" value="{email}" required>
      </div>

      <!-- Message -->
      <div class="form-group">
        <label for="description">Message</label>
        <input type="text" id="message" name="message" value="{message}" required>
      </div>

      <!-- Submit Button -->
      <button type="submit" class="submit-btn">Update Volunteer</button>
    </form>
  </div>
''')
print('''
  
</body>
</html>
''')
