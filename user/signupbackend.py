#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
print("Content-Type:text/html\n")
import mysql.connector
form=cgi.FieldStorage()
#print(form)
fullname=form.getvalue("fullname")
#print(fullname)
email=form.getvalue("email")
#print(email)
phonenumber=form.getvalue("phonenumber")
#print(phonenumber)
DateofBirth=form.getvalue("DateofBirth")
#print(DateofBirth)
password=form.getvalue("password")
#print(password)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="jeevankiran")
mycursor = mydb.cursor()
query =f"""INSERT INTO `signup`(`fullname`, `email`, `phonenumber`, `DateofBirth`, `password`) VALUES ('{fullname}','{email}','{phonenumber}','{DateofBirth}','{password}')"""
#print(query)
mycursor.execute(query)
mydb.commit()
print(f'''<script>alert("Registered Successfully!");
    location.href="login.py";
    </script>''')
