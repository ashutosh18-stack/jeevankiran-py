#!C:\Python312\python.exe
import cgi
import cgitb
import mysql.connector
import os
import sys
cgitb.enable()
print("Content-Type: text/html\n")
form = cgi.FieldStorage()
#print(form)
id = form.getvalue('id')
fullname = form.getvalue('fullname')
email = form.getvalue('email')
phonenumber = form.getvalue('phonenumber')
DateofBirth = form.getvalue('DateofBirth')
password = form.getvalue('password')
confirm_password = form.getvalue('confirm_password')
if not id:
    print("<h3 style='color:red;'>Unauthorized access. Please login first.</h3>")
    sys.exit()
if password != confirm_password:
    print("<h3 style='color:red;'>Passwords do not match!</h3>")
    sys.exit()
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="jeevankiran"
    )
    cursor = mydb.cursor()

    # Use parameterized query to prevent SQL injection
    update_query = """
    UPDATE usersignup SET fullname=%s, email=%s, phonenumber=%s, DateofBirth=%s, password=%s WHERE id=%s
    """
    values = (fullname, email, phonenumber, DateofBirth, password, id)
    cursor.execute(update_query, values)
    mydb.commit()
    

    if cursor.rowcount == 1:
           print(f'''<script>
        alert("Profile Edited Successful!");
        localStorage.clear();
        location.href = "userlogin.py";
    </script>''')
        
    else:
       print(f'''<script>
        alert("Profile Edit Unsuccessful!");
        location.href = "index.py";
    </script>''')
       

except mysql.connector.Error as err:
    print(f"<h3 style='color:red;'>Database error: {err}</h3>")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
