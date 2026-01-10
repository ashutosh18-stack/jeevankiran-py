#!C:/Python312/python.exe
import cgi, mysql.connector

print("Content-Type: text/html\n")

form = cgi.FieldStorage()

donation_id = form.getvalue("donation_id")
razorpay_payment_id = form.getvalue("razorpay_payment_id")
razorpay_order_id = form.getvalue("razorpay_order_id")

# Basic validation
if not donation_id or not razorpay_payment_id or not razorpay_order_id:
    print("<h3 style='color:red;text-align:center;'>Invalid Payment Details</h3>")
    exit()

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="jeevankiran"
    )
    cursor = db.cursor()

    cursor.execute(
        """
        UPDATE donate_payment
        SET payment_status = 'paid',
            razorpay_payment_id = %s,
            razorpay_order_id = %s,
            payment_date = NOW()
        WHERE donation_id = %s
        """,
        (razorpay_payment_id, razorpay_order_id, donation_id)
    )

    if cursor.rowcount == 0:
        print("<h3 style='color:red;text-align:center;'>Donation ID Not Found</h3>")
    else:
        db.commit()

        # Redirect to receipt page
        print(f"""
        <html>
        <head>
            <meta http-equiv="refresh" content="0;url=donation_receipt.py?donation_id={donation_id}">
        </head>
        <body></body>
        </html>
        """)

except Exception as e:
    print(f"<h3 style='color:red;text-align:center;'>Error: {e}</h3>")

finally:
    cursor.close()
    db.close()
