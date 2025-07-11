#!C:/Python312/python.exe
import cgi
import cgitb
import header
import mysql.connector

cgitb.enable()
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="jeevankiran"
)
mycursor = mydb.cursor()


query = "SELECT * FROM ngomaster"
mycursor.execute(query)
results = mycursor.fetchall()

# HTML Header
print('''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>NGO List</title>
  <link rel="stylesheet" href="style/ngomasterlist.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
</head>
<body>
  <div class="ngo-list-container">
    <h2><i class="fas fa-list"></i> NGO List</h2>
    <table>
      <thead>
        <tr>
          <th>Id</th>
          <th>Name</th>
          <th>Email</th>
          <th>Phone</th>
          <th>Logo</th>
          <th>Description</th>
          <th>Address</th>
          <th>Social Links</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
''')

# Loop through NGOs
for x in results:
    print(f'''
        <tr>
          <td>{x[0]}</td>
          <td>{x[1]}</td>
          <td>{x[2]}</td>
          <td>{x[3]}</td>
          <td><img src="{x[4]}" alt="Logo" width="50" height="50" style="border-radius:6px;"></td>
          <td>{x[5]}</td>
          <td>{x[6]}</td>
          <td class="social-links">
            <a href="{x[7]}" target="_blank"><i class="fab fa-instagram"></i></a>
            <a href="{x[8]}" target="_blank"><i class="fab fa-twitter"></i></a>
            <a href="{x[9]}" target="_blank"><i class="fab fa-facebook"></i></a>
          </td>
          <td class="actions">
            <a href="editngo.py?id={x[0]}" class="edit"><i class="fas fa-edit"></i></a>
            <a href="deletengo.py?id={x[0]}" class="delete" onclick="return confirm('Are you sure to delete this NGO?');"><i class="fas fa-trash-alt"></i></a>
          </td>
        </tr>
    ''')


print('''
      </tbody>
    </table>
  </div>
</body>
</html>
''')
