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

query = "SELECT * FROM usersignup"
mycursor.execute(query)
results = mycursor.fetchall()

# HTML Header
print('''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Donor List</title>
  <link rel="stylesheet" href="style/ngomasterlist.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
  <style>
    .receipt-btn {
      background: #27ae60;
      color: white;
      padding: 6px 10px;
      border-radius: 5px;
      font-size: 12px;
      text-decoration: none;
    }

    .receipt-btn:hover {
      background: #1e8a4d;
    }
  </style>
</head>
<body>
  <div class="ngo-list-container">
    <h2><i class="fas fa-list"></i> Donor List</h2>
    <table>
      <thead>
        <tr>
          <th>ID</th> 
          <th>NAME</th>
          <th>EMAIL</th>
          <th>DOB</th>
          <th>REGISTRATION_DATE</th>
        </tr>
      </thead>
      <tbody>
''')

# Loop
for x in results:
    id = x['id']
    name = x['fullname']
    email = x['email']
    amount = x['DateofBirth']
    message = x['regdate']

    print(f'''
      <tr>
        <td>{id}</td>
        <td>{name}</td>
        <td>{email}</td>
        <td>{amount}</td>
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
