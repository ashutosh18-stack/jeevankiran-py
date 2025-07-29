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

query = "SELECT * FROM Campaignmaster"
mycursor.execute(query)
results = mycursor.fetchall()

# HTML Header
print('''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Campaign List</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
   <link rel="stylesheet" href="style/projectlist.css">

</head>
<body>
  <div class="ngo-list-container">
    <h2><i class="fas fa-list"></i> Campaign List</h2>
    <table>
      <thead>
        <tr>
          <th>ID</th> 
          <th>Images</th>
          <th>Title</th>
          <th>Description</th>
          <th>Status</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
''')

# Loop through campaign
for x in results:
    id = x['id']
    title = x['title']
    desc = x['description']
    status = x['status']
    img1 = x['img1']
    img2 = x['img2']
    img3 = x['img3']

    # Folder is named using id
    folder = str(id)

    img_html = '<div class="campaign-img-group">'
    for i, img in enumerate([img1, img2, img3], start=1):
        if img:
            img_path = f"backend/campaignuploads/{folder}/{img}"
            img_html += f'<img src="{img_path}" alt="Image {i}">'
    img_html += '</div>'

    # Print Campaign row
    print(f'''
      <tr>
        <td>{id}</td>
        <td>{img_html}</td>
        <td>{title}</td>
        <td><div class="desc-cell">{desc}</div></td>
        <td>{status}</td>
        <td class="actions">
          <a href="Campaignedit.py?id={id}" class="edit"><i class="fas fa-edit"></i></a>
          <a href="backend/Campaignmasterdelete.py?id={id}" class="delete"><i class="fas fa-trash-alt"></i></a>
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
