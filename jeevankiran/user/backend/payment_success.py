#!C:\Python312\python.exe
print("Content-type: text/html\n")

import cgi, cgitb
cgitb.enable()
import mysql.connector

form = cgi.FieldStorage()
donation_id = form.getvalue("donation_id")
payment_id = form.getvalue("payment_id")

# Connect DB
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
cursor = mydb.cursor()

# Update payment status
cursor.execute("UPDATE donations SET payment_status=%s WHERE id=%s", ("success", donation_id))
mydb.commit()

print(f"""
<html>
<head><title>Donation Successful</title></head>
<body>
<h2>🎉 Thank you! Your donation was successful.</h2>
<p>Donation ID: {donation_id}</p>
<p>Payment ID: {payment_id}</p>
<a href="index.html">Back to Home</a>
</body>
</html>
""")
