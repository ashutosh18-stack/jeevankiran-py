#!C:\Python312\python.exe
import cgi
import cgitb
import mysql.connector
import http.cookies
import os

cgitb.enable()

form = cgi.FieldStorage()
phonenumber = form.getvalue("phonenumber") 
password = form.getvalue("password")

# --- Database connection ---
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="jeevankiran"
)
mycursor = mydb.cursor()
query = "SELECT * FROM `usersignup` WHERE `phonenumber`=%s AND `password`=%s"
mycursor.execute(query, (phonenumber, password))
myresult = mycursor.fetchone()

if myresult:
    user_id = myresult[0]
    fullname = myresult[2]

    # --- Create session file ---
    sessions_folder = os.path.join(os.path.dirname(__file__), "../sessions")
    if not os.path.exists(sessions_folder):
        os.makedirs(sessions_folder)

    session_file = os.path.join(sessions_folder, f"{user_id}.txt")
    with open(session_file, "w") as f:
        f.write(str(user_id))

    # --- Set cookie ---
    cookie = http.cookies.SimpleCookie()
    cookie["id"] = str(user_id)
    cookie["id"]["path"] = "/"  # valid for whole site

    print("Content-Type: text/html")
    print(cookie.output())  # set-cookie header
    print()  # end headers

    print(f'''<script>
        localStorage.clear();
        localStorage.setItem("id", '{user_id}');
        localStorage.setItem("fullname", '{fullname}');
        alert("Welcome User-{fullname}!");
        location.href = "../index.py?id={user_id}";
    </script>''')

else:
    print("Content-Type: text/html\n")
    print(f'''<script>
        alert("Login Unsuccessful!");
        location.href = "../userlogin.py";
    </script>''')
