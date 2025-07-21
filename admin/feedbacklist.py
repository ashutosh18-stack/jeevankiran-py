#!C:/Python312/python.exe
import cgi
import cgitb
import header
import mysql.connector
import os

cgitb.enable()

# Connect DB
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
mycursor = mydb.cursor(dictionary=True)

query = "SELECT * FROM contact"
mycursor.execute(query)
results = mycursor.fetchall()

# HTML Header
print('''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Project List</title>
  <link rel="stylesheet" href="style/ngomasterlist.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
  <style>
    .project-img-group {
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
    }
    .project-img-group img {
      width: 60px;
      height: 60px;
      object-fit: cover;
      border-radius: 6px;
      border: 1px solid #ddd;
    }
    td.actions a {
      margin-right: 6px;
      color: #444;
      font-size: 16px;
    }
  </style>
</head>
<body>
  <div class="ngo-list-container">
    <h2><i class="fas fa-list"></i> Volunteer List</h2>
    <table>
      <thead>
        <tr>
          <th>ID</th> 
          <th>NAME</th>
          <th>EMAIL</th>
          <th>SUBJECT</th>
          <th>MESSAGE</th>
          
        </tr>
      </thead>
      <tbody>
''')

# Loop through projects
for x in results:
    id = x['id']
    name = x['name']
    email = x['email']
    subject = x['subject']
    message = x['message']
    

    print(f'''
      <tr>
        <td>{id}</td>
        <td>{name}</td>
        <td>{email}</td>
        <th>{subject}</td>
        <td>{message}</td>
        
      </tr>
    ''')

print('''
      </tbody>
    </table>
  </div>
</body>
</html>
''')
