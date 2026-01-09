#!C:/Python312/python.exe
import cgi
import cgitb
cgitb.enable()

import mysql.connector
import sys, io

# UTF-8 support
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Read form data
form = cgi.FieldStorage()

user_id = form.getvalue("userid")
name = form.getvalue("name")
email = form.getvalue("email")
amount = form.getvalue("amount")
message = form.getvalue("message")

# DB connection
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

    values = (
        user_id,
        name,
        email,
        amount,
        message,
        "pending"
    )

    cursor.execute(sql, values)
    mydb.commit()

    donation_id = cursor.lastrowid  # useful for next steps

    cursor.close()
    mydb.close()

    # Redirect to confirmation page
    print("Status: 302 Found")
    print(f"Location: donation_confirm.py?donation_id={donation_id}")
    print()

except Exception as e:
    print("Content-Type: text/html\n")
    print("<h2>Error occurred</h2>")
    print("<pre>", e, "</pre>")
