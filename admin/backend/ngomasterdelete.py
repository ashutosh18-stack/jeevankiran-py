#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
print("Content-Type:text/html\n")
import mysql.connector
form=cgi.FieldStorage()
ngo_id =form.getvalue("ngo_id")
# ngo_name =form.getvalue("ngo_name")
# print(ngo_name)
# print(ngo_id)
mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "",
    database = "jeevankiran"
)
mycursor = mydb.cursor()
query=(f''' DELETE FROM ngomaster WHERE ngo_id = {ngo_id}''')
# print(query)
mycursor.execute(query)
mydb.commit()
print(f'''<script>alert(" NGO Deleted Successfully!");
    location.href="../ngomasterlist.py";
    </script>''') 
