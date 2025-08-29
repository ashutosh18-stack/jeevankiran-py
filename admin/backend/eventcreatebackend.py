#!C:/Python312/python.exe
import cgi
import cgitb
cgitb.enable()
import os
import mysql.connector
print("Content-Type:text/html\n")
form=cgi.FieldStorage()
title=form.getvalue('title')
# print(title)
event_description=form.getvalue('description')
event_objectives=form.getvalue('objectives')
event_yourhelp=form.getvalue('yourhelp')
event_contribution=form.getvalue('contribution')
event_impact = form.getvalue("impact")
fi=form["eventImage"]
fn=os.path.splitext(fi.filename)

uploadFileName=f'event'+fn[1]
mydb=mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "jeevankiran"
)
mycursor=mydb.cursor()
query=f''' SELECT id FROM campaignmaster where title="{title}"'''

mycursor.execute(query)
data= mycursor.fetchone()
#print(id)
insert_query=f''' INSERT INTO eventmaster(id ,title,description,objectives,yourhelp,img,contribution,impact) 
VALUES('{id}','{title}','{event_description}','{event_objectives}','{event_yourhelp}','{uploadFileName}','{event_contribution}','{event_impact}') '''
#print(insert_query)
mycursor.execute(insert_query)
mydb.commit()
id=mycursor.lastrowid
upload_dir=f"eventuploads/{id}"
os.makedirs(upload_dir,exist_ok=True)
file_path = os.path.join(upload_dir,uploadFileName)
open(file_path, 'wb').write(fi.file.read())
print(f''' 
<script>alert("Event added succesfully!")
      location.href="../eventlist.py"</script>''')