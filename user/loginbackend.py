#!C:\Python312\python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Context-Type:text/html\n")
form=cgi.FieldStorage()
#print(form)
fullname=form.getvalue("fullname")
#print(fullname)
phonenumber=form.getvalue("phonenumber") 
#print(phonenumber)
password=form.getvalue("password")
#print(password)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="jeevankiran")
mycursor = mydb.cursor()
query=f"""SELECT * FROM `signup` WHERE `phonenumber`='{phonenumber}' AND `password`='{password}'"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchone()
#print(myresult)
#print(mycursor.rowcount)
if mycursor.rowcount == 1:
    id=myresult[0];
    fullname=myresult[1];
    print(f'''<script>
        localStorage.clear()
        localStorage.setItem("id",'{id}')
        localStorage.setItem("fullname",'{fullname}')
        alert("Welcome User-{fullname}!");
        location.href="index.py";
    </script>''')
else:
    print(f'''<script>
        alert("Login Unsuccessfully!");
        location.href="login.py";
    </script>''')


