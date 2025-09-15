#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
import mysql.connector
print("Content-Type:text/html\n")
form=cgi.FieldStorage()
# print(form)
admin_id=form.getvalue("admin_id")
admin_first_name=form.getvalue("first_name")
# print(admin_first_name)
admin_middle_name=form.getvalue("middle_name")
# print(admin_middle_name)
admin_last_name=form.getvalue("last_name")
# print(admin_last_name)
admin_address=form.getvalue("address")
# print(admin_address)
admin_email=form.getvalue("email")
admin_DOB=form.getvalue("dob")
# print(admin_email)
admin_phone=form.getvalue("phone")
# print(admin_phone)
admin_password=form.getvalue("new_password")
# print(admin_password)
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
mycursor=mydb.cursor()
query=f"""UPDATE adminlogin SET admin_first_name='{admin_first_name}', admin_middle_name='{admin_middle_name}', admin_last_name='{admin_last_name}', admin_address='{admin_address}', admin_email='{admin_email}',admin_DOB='{admin_DOB}', admin_phone='{admin_phone}', admin_password='{admin_password}' WHERE admin_id={admin_id}"""
# print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
      <script>
      alert("profile updated successfully!");
      location.href="../dashboard.py?admin_id={admin_id}";
      </script>''')