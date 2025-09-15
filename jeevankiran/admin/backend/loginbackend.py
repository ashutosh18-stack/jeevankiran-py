#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
import mysql.connector
print("Content-Type: text/html\n")
form=cgi.FieldStorage()
#print(form)
admin_id=form.getvalue("admin_id")
admin_email=form.getvalue("email")
admin_phone=form.getvalue("phone")
admin_password=form.getvalue("password")
#print(admin_password)
mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
mycursor=mydb.cursor()
query=f"""SELECT * FROM adminlogin where admin_phone='{admin_phone}' AND admin_password='{admin_password}'"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchone()
#print(myresult)
#print(mycursor.rowcount)
if mycursor.rowcount==1:
    admin_id=myresult[0];
    admin_name=myresult[1];
    admin_phone=myresult[3];
    admin_password=myresult[4];
    print(f''' 
          <script>
          localStorage.clear();
          localStorage.setItem("admin_phone","{admin_phone}");
          localStorage.setItem("admin_password","{admin_password}");
          
          alert("welcome {admin_name}");
          location.href="../dashboard.py?admin_id={admin_id}";
          </script>''')
else:
    print(f'''
    <script>alert("login unsuccessfully!");
    location.href="../login.py";
    </script>''')