#!C:/Python312/python.exe
import cgi, cgitb
import mysql.connector
from datetime import datetime

cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
package_id = form.getvalue("package_id")
payment_id = form.getvalue("payment_id")

mydb = mysql.connector.connect(
    host="localhost", user="root", password="", database="jeevankiran")
cursor = mydb.cursor()

# Corrected query without unintended indentation or newline formatting issues
query = (
    "UPDATE package_donations "
    "SET payment_status=%s, payment_date=%s, receipt_path=%s "
    "WHERE id=%s"
)

params = ('success', datetime.now(), f"receipt_{payment_id}.pdf", package_id)

cursor.execute(query, params)

mydb.commit()
cursor.close()
mydb.close()

print("<h2>Payment Successful</h2>")
print(f"<p>Thank you! Your payment ID: {payment_id}</p>")
