#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
import mysql.connector
import sys, io, html, datetime
import razorpay

# Ensure UTF-8 output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
print("Content-Type: text/html; charset=utf-8\n")

# ---------- Razorpay + DB Config ----------
RAZORPAY_KEY_ID = "rzp_test_RDxnTJFjtdr936"
RAZORPAY_KEY_SECRET = "1zg6Nmrq4VcVmJK5SOAI7uTz"

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "jeevankiran"
}
# ------------------------------------------

def show_message(title, message):
    print(f"""<!doctype html>
    <html><head><meta charset="utf-8"><title>{html.escape(title)}</title></head>
    <body style="font-family:Arial;padding:30px;">
      <h2>{html.escape(title)}</h2>
      <p>{html.escape(message)}</p>
    </body></html>""")
    sys.exit(0)

form = cgi.FieldStorage()

donated_id = form.getfirst("donated_id")
razorpay_payment_id = form.getfirst("razorpay_payment_id")
razorpay_order_id = form.getfirst("razorpay_order_id")
razorpay_signature = form.getfirst("razorpay_signature")

if not donated_id:
    show_message("Payment Failed", "No Donation ID provided!")

db = mysql.connector.connect(**DB_CONFIG)
cursor = db.cursor()

client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))

# Verify signature
verified = False
try:
    client.utility.verify_payment_signature({
        "razorpay_order_id": razorpay_order_id,
        "razorpay_payment_id": razorpay_payment_id,
        "razorpay_signature": razorpay_signature
    })
    verified = True
except:
    verified = False

# Current timestamp
payment_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if verified:
    cursor.execute("""
        UPDATE package_payment 
        SET payment_status=%s, payment_date=%s, transaction_id=%s, razorpay_order_id=%s
        WHERE donated_id=%s
    """, ("success",  payment_time, razorpay_payment_id, razorpay_order_id, donated_id))
    if cursor.rowcount == 0:
        cursor.execute("""
            UPDATE package_payment 
            SET payment_status=%s, payment_date=%s, transaction_id=%s, razorpay_order_id=%s
            WHERE id=%s
        """, ("success", payment_time, razorpay_payment_id, razorpay_order_id, donated_id))
    db.commit()

    # Redirect to receipt page
    print(f"""<html><head>
      <meta http-equiv="refresh" content="0;url=receipt.py?donated_id={donated_id}">
    </head><body>
      <p>Redirecting to receipt...</p>
    </body></html>""")

else:
    cursor.execute("""
        UPDATE package_payment 
        SET payment_status=%s, payment_date=%s 
        WHERE donated_id=%s
    """, ("failed", payment_time, donated_id))
    if cursor.rowcount == 0:
        cursor.execute("""
            UPDATE package_payment 
            SET payment_status=%s, payment_date=%s 
            WHERE id=%s
        """, ("failed", payment_time, donated_id))
    db.commit()

    show_message("Payment Failed", "Your payment could not be verified. Please try again.")
