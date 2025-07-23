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

query = "SELECT * FROM projectmaster"
mycursor.execute(query)
results = mycursor.fetchall()

# HTML Header
print('''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Project List</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
   <link rel="stylesheet" href="style/projectlist.css">

</head>
<body>
  <div class="ngo-list-container">
    <h2><i class="fas fa-list"></i> Project List</h2>
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

# Loop through projects
for x in results:
    project_id = x['project_id']
    title = x['project_title']
    desc = x['project_description']
    status = x['status']
    img1 = x['project_img1']
    img2 = x['project_img2']
    img3 = x['project_img3']

    # Folder is named using project_id
    folder = str(project_id)

    img_html = '<div class="project-img-group">'
    for i, img in enumerate([img1, img2, img3], start=1):
        if img:
            img_path = f"backend/projectuploads/{folder}/{img}"
            img_html += f'<img src="{img_path}" alt="Image {i}">'
    img_html += '</div>'

    # Print project row
    print(f'''
      <tr>
        <td>{project_id}</td>
        <td>{img_html}</td>
        <td>{title}</td>
        <td><div class="desc-cell">{desc}</div></td>
        <td>{status}</td>
        <td class="actions">
          <a href="projectedit.py?project_id={project_id}" class="edit"><i class="fas fa-edit"></i></a>
          <a href="backend/projectmasterdelete.py?project_id={project_id}" class="delete"><i class="fas fa-trash-alt"></i></a>
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
