#!C:/Python312/python.exe
import cgi
import cgitb
cgitb.enable()

import mysql.connector
import razorpay
import sys, io

# UTF-8 support
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print("Content-Type: text/html; charset=utf-8\n")

form = cgi.FieldStorage()
donation_id = form.getvalue("donation_id")

if not donation_id:
    print("<h3>Donation ID missing</h3>")
    sys.exit()

# ---------- DB CONNECTION ----------
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="jeevankiran"
    )
    cursor = mydb.cursor(dictionary=True)

    cursor.execute("""
        SELECT donation_id, name, email, amount 
        FROM donate_payment 
        WHERE donation_id=%s
    """, (donation_id,))

    donation = cursor.fetchone()

    cursor.close()
    mydb.close()

    if not donation:
        print("<h3>Invalid Donation</h3>")
        sys.exit()

except Exception as e:
    print("<pre>", e, "</pre>")
    sys.exit()

# ---------- RAZORPAY CONFIG ----------
KEY_ID = "rzp_test_RxWTJWtTw0k7lD"
KEY_SECRET = "PEdKzBx27Hd7ziiJo3JXsB1h"

client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))

amount_paise = int(float(donation['amount']) * 100)

order = client.order.create({
    "amount": amount_paise,
    "currency": "INR",
    "payment_capture": 1
})

# ---------- PAYMENT PAGE ----------
print(f"""
<!DOCTYPE html>
<html>
<head>
    <title>Donate Payment</title>
    <script src="https://checkout.razorpay.com/v1/checkout.js"></script>
</head>
<body>

<h2 style="text-align:center;">Redirecting to Secure Payment...</h2>

<script>
var options = {{
    "key": "{KEY_ID}",
    "amount": "{amount_paise}",
    "currency": "INR",
    "name": "JeevanKiran NGO",
    "description": "Donation Payment",
    "order_id": "{order['id']}",
    "handler": function (response) {{
        window.location.href =
        "donation_payment_status.py"
        + "?donation_id={donation['donation_id']}"
        + "&razorpay_payment_id=" + response.razorpay_payment_id
        + "&razorpay_order_id=" + response.razorpay_order_id
        + "&razorpay_signature=" + response.razorpay_signature;
    }},
    "prefill": {{
        "name": "{donation['name']}",
        "email": "{donation['email']}"
    }},
    "theme": {{
        "color": "#3399cc"
    }}
}};
var rzp1 = new Razorpay(options);
rzp1.open();
</script>

</body>
</html>
""")
