#!C:/Python312/python.exe
import cgi
import cgitb
cgitb.enable()

import mysql.connector
import sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form = cgi.FieldStorage()

user_id = form.getvalue("userid")
name = form.getvalue("name")
email = form.getvalue("email") 
amount = form.getvalue("amount")
message = form.getvalue("message")

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="jeevankiran"
    )
    cursor = mydb.cursor()

    sql = """
        INSERT INTO donate_payment
        (user_id, name, email, amount, message, payment_status)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    cursor.execute(sql, (user_id, name, email, amount, message, "pending"))
    mydb.commit()

    donation_id = cursor.lastrowid
    cursor.close()
    mydb.close()

    print("Status: 302 Found")
    print(f"Location: donation_confirm.py?donation_id={donation_id}")
    print()

except mysql.connector.Error as err:
    print("Content-Type: text/html\n")
    print("<h2>MySQL Error</h2>")
    print(f"<pre>{err}</pre>")

except Exception as e:
    print("Content-Type: text/html\n")
    print("<h2>Unexpected Error</h2>")
    print(f"<pre>{e}</pre>")
