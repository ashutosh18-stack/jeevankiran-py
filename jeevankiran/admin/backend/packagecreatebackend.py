#!C:/Python312/python.exe
import cgi
import cgitb
cgitb.enable()
import os
import mysql.connector
print("Content-Type:text/html\n")
form=cgi.FieldStorage()
project_name=form.getvalue('project')
# print(project_name)
package_item=form.getvalue('item')
package_qty=form.getvalue('qty')
package_price=form.getvalue('price')
package_descrip=form.getvalue('description')
package_status = form.getvalue("status")
fi=form["packageImage"]
fn=os.path.splitext(fi.filename)

uploadFileName=f'package'+fn[1]
mydb=mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "jeevankiran"
)
mycursor=mydb.cursor()
project_query=f''' SELECT project_id FROM projectmaster where project_title="{project_name}"'''

mycursor.execute(project_query)
project_data= mycursor.fetchone()
project_id = project_data[0] if project_data else None
# print(project_id)
insert_query=f''' INSERT INTO packagemaster(project_id ,package_item,package_qty,package_price,	package_description,package_img,package_status) 
VALUES('{project_id}','{package_item}','{package_qty}','{package_price}','{package_descrip}','{uploadFileName}','{package_status}') '''
# print(insert_query)
mycursor.execute(insert_query)
mydb.commit()
package_id=mycursor.lastrowid
upload_dir=f"packageuploads/{package_id}"
os.makedirs(upload_dir,exist_ok=True)
file_path = os.path.join(upload_dir,uploadFileName)
open(file_path, 'wb').write(fi.file.read())
print(f''' 
<script>alert("package added succesfully!")
      location.href="../packagemaster.py"</script>''')