#!C:/Python312/python.exe

import cgi
import cgitb
import os
import mysql.connector

cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
package_id = form.getvalue("package_id")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
mycursor = mydb.cursor()

folder_path = f"packageuploads/{package_id}"

if os.path.exists(folder_path):
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))
    os.rmdir(folder_path)

delete_package_query = f"DELETE FROM packagemaster WHERE package_id ={package_id}"
# print(delete_package_query)
mycursor.execute(delete_package_query)
mydb.commit()



print(f'''<script>alert("Package Deleted successfully");
      location.href="../packagelist.py"</script> ''')
