#!C:\Python312\python.exe
import cgi
import cgitb
from datetime import datetime
import mysql.connector

cgitb.enable()

form = cgi.FieldStorage()
donor_name = form.getvalue("donor_name")
amount = form.getvalue("amount")
payment_mode = form.getvalue("payment_mode")
purpose = form.getvalue("purpose")

# Generate receipt number & date
receipt_no = "R" + datetime.now().strftime("%Y%m%d%H%M%S")
today = datetime.now().strftime("%Y-%m-%d")

# Save in database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
cur = conn.cursor()
cur.execute(
    "INSERT INTO receipts (receipt_no, donor_name, amount, payment_mode, purpose, date) VALUES (%s,%s,%s,%s,%s,%s)",
    (receipt_no, donor_name, amount, payment_mode, purpose, today)
)
conn.commit()
cur.close()
conn.close()

# Show receipt
print("Content-Type: text/html\n")
print(f"""
<h2>Donation Receipt</h2>
<p>Receipt No: {receipt_no}</p>
<p>Date: {today}</p>
<p>Donor Name: {donor_name}</p>
<p>Amount: ₹{amount}</p>
<p>Payment Mode: {payment_mode}</p>
<p>Purpose: {purpose}</p>
<p>Thank you for your generous donation!</p>
""")
