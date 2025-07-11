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
mycursor = mydb.cursor(dictionary=True)


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
      <th>Logo</th>
          <th>Name</th>
          <th>Email</th>
          <th>Phone</th>
         
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
          <td>{x['ngo_id']}</td>
           <td><img src="backend/ngomasteruploads/{x['ngo_logo']}" alt="Logo" width="50" height="50" style="border-radius:6px;"></td>       
          <td>{x['ngo_name']}</td>
          <td>{x['ngo_email']}</td>
          <td>{x['ngo_phone']}</td>

       <td>{x['ngo_description']}</td>
          <td>{x['ngo_address']}</td>
          <td class="social-links">
            <a href="{x['ngo_instagram']}" target="_blank"><i class="fab fa-instagram"></i></a>
            <a href="{x['ngo_twitter']}" target="_blank"><i class="fab fa-twitter"></i></a>
            <a href="{x['ngo_facebook']}" target="_blank"><i class="fab fa-facebook"></i></a>
          </td>
          <td class="actions">
            <a href="ngomasteredit.py?ngo_id={x['ngo_id']}" class="edit"><i class="fas fa-edit"></i></a>
            <a href="backend/ngomasterdelete.py?ngo_id={x['ngo_id']}" class="delete" ><i class="fas fa-trash-alt"></i></a>
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
