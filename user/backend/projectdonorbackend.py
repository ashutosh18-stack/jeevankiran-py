#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
import os

from datetime import datetime
cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()

# Get form data
user_id = form.getvalue("userid")
package_id = form.getvalue("package_id")
user_name = form.getvalue("name")
user_email = form.getvalue("email")
package_item = form.getvalue("item")
quantity = int(form.getvalue("quantity") or 1)
amount = float(form.getvalue("amount") or 0)
message = form.getvalue("message")

# Payment values (set default)
payment_status = 'pending'
payment_date = None  # Will be updated after success

# Connect to DB
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
cursor = mydb.cursor()

# Insert into package_donations table (without receipt path)
query = """
    INSERT INTO package_donations (
        user_id, package_id, quantity, amount, message, payment_status
    ) VALUES (%s, %s, %s, %s, %s, %s)
"""
values = (user_id, package_id, quantity, amount, message, payment_status)

cursor.execute(query, values)
mydb.commit()

# Get the inserted donation ID
donation_id = cursor.lastrowid

# Redirect to payment gateway with donation_id
print(f'''
<script>
    window.location.href = "../payment_gateway.py?package_id={package_id}";
</script>
''')
