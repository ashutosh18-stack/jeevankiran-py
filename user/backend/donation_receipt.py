#!C:/Python312/python.exe
import cgi, cgitb
cgitb.enable()

import mysql.connector
import sys, io

# UTF-8 support
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
print("Content-Type: text/html; charset=utf-8\n")

form = cgi.FieldStorage()
donation_id = form.getvalue("donation_id")

if not donation_id:
    print("<h3 style='text-align:center;color:red;'>Donation ID Missing</h3>")
    sys.exit()

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="jeevankiran"
    )
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT donation_id, name, email, amount,
               razorpay_order_id, razorpay_payment_id,
               payment_date
        FROM donate_payment
        WHERE donation_id=%s AND payment_status='paid'
    """, (donation_id,))

    data = cursor.fetchone()

    if not data:
        print("<h3 style='text-align:center;color:red;'>Receipt Not Found</h3>")
        sys.exit()

except Exception as e:
    print("<pre>", e, "</pre>")
    sys.exit()

finally:
    cursor.close()
    db.close()

print(f"""
<!DOCTYPE html>
<html>
<head>
<title>Donation Receipt</title>

<style>
body {{
    font-family: Arial, sans-serif;
    background: #f2f2f2;
}}
.receipt-box {{
    width: 700px;
    margin: 50px auto;
    background: #fff;
    padding: 30px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}}
h2 {{
    text-align: center;
    color: #2c7a7b;
}}
table {{
    width: 100%;
    margin-top: 20px;
}}
td {{
    padding: 10px;
    border-bottom: 1px solid #ddd;
}}
.label {{
    font-weight: bold;
}}
.actions {{
    text-align: center;
    margin-top: 30px;
}}
button {{
    padding: 12px 25px;
    background: #2c7a7b;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
}}
</style>

</head>
<body>

<div class="receipt-box">
    <h2>Donation Receipt</h2>

    <table>
        <tr><td class="label">Donation ID</td><td>{data['donation_id']}</td></tr>
        <tr><td class="label">Name</td><td>{data['name']}</td></tr>
        <tr><td class="label">Email</td><td>{data['email']}</td></tr>
        <tr><td class="label">Amount</td><td>₹ {data['amount']}</td></tr>
        <tr><td class="label">Razorpay Order ID</td><td>{data['razorpay_order_id']}</td></tr>
        <tr><td class="label">Razorpay Payment ID</td><td>{data['razorpay_payment_id']}</td></tr>
        <tr><td class="label">Payment Date</td><td>{data['payment_date']}</td></tr>
    </table>

    <div class="actions">
         <button onclick="window.location.href='donation_receipt_pdf.py?donation_id={data['donation_id']}'">Download PDF</button>

        <button onclick="window.location.href='../index.py'">Go to Home</button>
    </div>
</div>

</body>
</html>
""")
