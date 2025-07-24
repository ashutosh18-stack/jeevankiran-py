#!C:\Python312\python.exe
import cgi
import cgitb
import os
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
regdate=form.getvalue("regdate")
#print(regdate)
fi=form["img"]
fn=os.path.splitext(fi.filename)
uploadFileName=f'profile'+fn[1]
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="jeevankiran")
mycursor = mydb.cursor()
query =f"""INSERT INTO `usersignup`(`img`,`fullname`, `email`, `phonenumber`, `DateofBirth`, `password`, `regdate`) VALUES ('{uploadFileName}','{fullname}','{email}','{phonenumber}','{DateofBirth}','{password}','{regdate}')"""
#print(query)
mycursor.execute(query)
mydb.commit()
profileid=mycursor.lastrowid
upload_dir=f"useruploads/{profileid}"
os.makedirs(upload_dir,exist_ok=True)
file_path=os.path.join(upload_dir,uploadFileName)
open(file_path,'wb').write(fi.file.read())
print(f'''<script>alert("Registered Successfully!");
    location.href="../userlogin.py";
    </script>''')
