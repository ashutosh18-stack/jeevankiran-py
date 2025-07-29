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
    eventmaster.id AS id,
    campaignmaster.title AS title,
    eventmaster.event_description,
    eventmaster.event_objectives,
    eventmaster.event_yourhelp,
    eventmaster.event_contribution,
    eventmaster.event_impact,
    eventmaster.event_img
FROM eventmaster
JOIN campaignmaster ON eventmaster.id = campaignmaster.id;
"""
mycursor.execute(query)
results = mycursor.fetchall()

print('''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Event List</title>
  <link rel="stylesheet" href="style/ngomasterlist.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

</head>
<body>
  <div class="ngo-list-container">
    <h2><i class="fas fa-list"></i> Event List</h2>
    <table>
      <thead>
        <tr>
           
          <th>Image</th>
          <th>Event Title</th>
          <th>Objectives</th>
          <th>Description</th>
          <th>Yourhelp</th>
          <th>Contribution</th>
          <th>Impact</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
''')

for x in results:
    id = x['id']
    title = x['title']
    objectives =x['objectives']
    description = x['description']
    yourhelp = x['yourhelp']
    contribution = x['contribution']
    impact = x['impact']
    img = x['event_img']

    folder = str(id)

    img_html = '<div class="campaign-img-group">'
    if img:
        img_path = f"backend/eventuploads/{folder}/{img}"
        img_html += f'<img src="{img_path}" alt="Image">'
    img_html += '</div>'

    print(f'''
      <tr>
        <td>{id}</td>
        <td>{img_html}</td>
        <td>{title}</td>
        <td>{description}</td>
        <td>{objectives}</td>
        <td>{yourhelp}</td>
        <td>{contribution}</td>
        <td>{impact}</td>
        <td class="actions">
          <a href="eventedit.py?id={id}" class="edit"><i class="fas fa-edit"></i></a>
          <a href="backend/eventmasterdelete.py?id={id}" class="delete"><i class="fas fa-trash-alt"></i></a>
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
