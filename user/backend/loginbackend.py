#!C:\Python312\python.exe
import cgi
import cgitb
import mysql.connector
import http.cookies

cgitb.enable()

form = cgi.FieldStorage()
fullname = form.getvalue("fullname")
phonenumber = form.getvalue("phonenumber") 
password = form.getvalue("password")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="jeevankiran"
)
mycursor = mydb.cursor()
query = f"""SELECT * FROM `signup` WHERE `phonenumber`='{phonenumber}' AND `password`='{password}'"""
mycursor.execute(query)
myresult = mycursor.fetchone()

if mycursor.rowcount == 1:
    id = myresult[0]
    fullname = myresult[1]

    cookie = http.cookies.SimpleCookie()
    cookie["id"] = str(id)  # set user id from DB
    cookie["id"]["path"] = "/"  # cookie valid for whole site

    print("Content-Type: text/html")
    print(cookie.output())  # set-cookie header
    print()  # end headers

    print(f'''<script>
        localStorage.clear();
        localStorage.setItem("id", '{id}');
        localStorage.setItem("fullname", '{fullname}');
        alert("Welcome User-{fullname}!");
        location.href = "index.py";
    </script>''')

else:
    print("Content-Type: text/html\n")
    print(f'''<script>
        alert("Login Unsuccessful!");
        location.href = "../login.py";
    </script>''')
