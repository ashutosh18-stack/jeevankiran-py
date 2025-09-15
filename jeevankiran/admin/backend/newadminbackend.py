#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
import mysql.connector
print("Content-Type: text/html\n")
form = cgi.FieldStorage()
# print(form)
first_name = form.getvalue("first_name")
# print(first_name)
middle_name = form.getvalue("middle_name")
# print(middle_name)
last_name = form.getvalue("last_name")
# print(last_name)
address = form.getvalue("address")
# print(address)
email = form.getvalue("email")
# print(email)
phone = form.getvalue("phone")
# print(phone)
new_password = form.getvalue("new_password")
# print(new_password)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
mycursor = mydb.cursor()
query = f"""INSERT INTO adminlogin (admin_first_name, admin_middle_name, admin_last_name, admin_address, admin_email, admin_phone, admin_password) 
           VALUES ('{first_name}', '{middle_name}', '{last_name}', '{address}', '{email}', '{phone}', '{new_password}')"""
# print(query)
mycursor.execute(query)   
mydb.commit()
print('''
      <script>
      alert("New admin added successfully!");
      location.href="../index.py";
      </script>''')