#!C:/Python312/python.exe
import cgi
import cgitb
import header
import mysql.connector
import os
import sys

cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')  # Fix UnicodeEncodeError

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
mycursor = mydb.cursor(dictionary=True)

query = """
SELECT 
    packagemaster.package_id AS package_id,
    projectmaster.project_title AS project_name,
    packagemaster.package_item,
    packagemaster.package_qty,
    packagemaster.package_price,
    packagemaster.package_description,
    packagemaster.package_status,
    packagemaster.package_img
FROM packagemaster
JOIN projectmaster ON packagemaster.project_id = projectmaster.project_id;
"""
mycursor.execute(query)
results = mycursor.fetchall()

print('''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Package List</title>
  <link rel="stylesheet" href="style/ngomasterlist.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

</head>
<body>
  <div class="ngo-list-container">
    <h2><i class="fas fa-list"></i> Package List</h2>
    <table>
      <thead>
        <tr>
          <th>ID</th> 
          <th>Images</th>
          <th>Project Title</th>
          <th>Package Name</th>
          <th>Qty</th>
          <th>Price</th>
          <th>Description</th>
          <th>Status</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
''')

for x in results:
    package_id = x['package_id']
    project_name = x['project_name']
    title = x['package_item']
    qty = x['package_qty']
    price = x['package_price']
    desc = x['package_description']
    status = x['package_status']
    img = x['package_img']

    folder = str(package_id)

    img_html = '<div class="project-img-group">'
    if img:
        img_path = f"backend/packageuploads/{folder}/{img}"
        img_html += f'<img src="{img_path}" alt="Image">'
    img_html += '</div>'

    print(f'''
      <tr>
        <td>{package_id}</td>
        <td>{img_html}</td>
        <td>{project_name}</td>
        <td>{title}</td>
        <td>{qty}</td>
        <td>{price}</td>
        <td class="desc-cell">{desc}</td>
        <td>{status}</td>
        <td class="actions">
          <a href="packageedit.py?package_id={package_id}" class="edit"><i class="fas fa-edit"></i></a>
          <a href="backend/packagemasterdelete.py?package_id={package_id}" class="delete"><i class="fas fa-trash-alt"></i></a>
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
