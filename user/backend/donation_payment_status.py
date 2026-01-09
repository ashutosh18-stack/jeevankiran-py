#!C:/Python312/python.exe
import cgi, cgitb
cgitb.enable()

import mysql.connector
import sys, io, os
from datetime import datetime

# UTF-8 output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
print("Content-Type: text/html; charset=utf-8\n")

from donation_receipt_pdf import generate_receipt_pdf

form = cgi.FieldStorage()

donation_id = form.getvalue("donation_id")
razorpay_payment_id = form.getvalue("razorpay_payment_id")
razorpay_order_id = form.getvalue("razorpay_order_id")

# Validation
if not donation_id or not razorpay_payment_id or not razorpay_order_id:
    print("<h3 style='color:red;text-align:center;'>Invalid Payment Details</h3>")
    sys.exit()

payment_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Absolute backend path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RECEIPT_FOLDER = os.path.join(BASE_DIR, "donation_receipt")

if not os.path.exists(RECEIPT_FOLDER):
    os.makedirs(RECEIPT_FOLDER)

pdf_filename = f"donation_{donation_id}.pdf"
pdf_full_path = os.path.join(RECEIPT_FOLDER, pdf_filename)

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="jeevankiran"
    )
    cursor = db.cursor()

    # 1️⃣ Update payment status
    cursor.execute("""
        UPDATE donate_payment
        SET payment_status = 'paid',
            razorpay_payment_id = %s,
            razorpay_order_id = %s,
            payment_date = %s,
            receipt_pdf = %s
        WHERE donation_id = %s
    """, (
        razorpay_payment_id,
        razorpay_order_id,
        payment_date,
        pdf_filename,
        donation_id
    ))

    if cursor.rowcount == 0:
        raise Exception("Donation ID not found")

    db.commit()

    # 2️⃣ Generate PDF (backend only)
    generate_receipt_pdf(donation_id, pdf_full_path)

    # 3️⃣ Redirect
    print(f"""
    <html>
    <head>
        <meta http-equiv="refresh" content="0;url=donation_receipt.py?donation_id={donation_id}">
    </head>
    <body></body>
    </html>
    """)

except Exception as e:
    db.rollback()
    print(f"<h3 style='color:red;text-align:center;'>Error: {e}</h3>")

finally:
    cursor.close()
    db.close()
