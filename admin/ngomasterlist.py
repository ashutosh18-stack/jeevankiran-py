#!C:/Python312/python.exe
import cgi
import cgitb
import header
import mysql.connector

cgitb.enable()


# DB Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # replace if you use a password
    database="jeevankiran"
)
mycursor = mydb.cursor(dictionary=True)

# Query data
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
          <th>#</th>
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
for i, row in enumerate(results, start=1):
    print(f'''
        <tr>
          <td>{i}</td>
          <td>{row['name']}</td>
          <td>{row['email']}</td>
          <td>{row['phone']}</td>
          <td><img src="{row['logo']}" alt="Logo" width="50" height="50" style="border-radius:6px;"></td>
          <td>{row['description']}</td>
          <td>{row['address']}</td>
          <td class="social-links">
            <a href="{row['instagram']}" target="_blank"><i class="fab fa-instagram"></i></a>
            <a href="{row['twitter']}" target="_blank"><i class="fab fa-twitter"></i></a>
            <a href="{row['facebook']}" target="_blank"><i class="fab fa-facebook"></i></a>
          </td>
          <td class="actions">
            <a href="editngo.py?id={row['id']}" class="edit"><i class="fas fa-edit"></i></a>
            <a href="deletengo.py?id={row['id']}" class="delete" onclick="return confirm('Are you sure to delete this NGO?');"><i class="fas fa-trash-alt"></i></a>
          </td>
        </tr>
    ''')

# HTML Footer
print('''
      </tbody>
    </table>
  </div>
</body>
</html>
''')
