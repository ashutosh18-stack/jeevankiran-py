#!C:\Python312\python.exe


import cgi
import cgitb
cgitb.enable()
import mysql.connector
import razorpay
import datetime
print("Content-type: text/html\n")
# Razorpay test keys (use your real keys in production)
RAZORPAY_KEY_ID = "rzp_test_RDxnTJFjtdr936"
RAZORPAY_KEY_SECRET = "1zg6Nmrq4VcVmJK5SOAI7uTz"

form = cgi.FieldStorage()

# Get form data
user_id = form.getvalue("userid")
package_id = form.getvalue("package_id")
user_name = form.getvalue("name")
user_email = form.getvalue("email")
item = form.getvalue("item")
quantity = int(form.getvalue("quantity"))
amount = float(form.getvalue("amount"))
message = form.getvalue("message")

# MySQL connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
cursor = mydb.cursor()

# Insert donation as pending
sql = """INSERT INTO donations 
(user_id, user_name, user_email, package_id, package_item, quantity, amount, message, payment_status, payment_date) 
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
values = (user_id, user_name, user_email, package_id, item, quantity, amount, message, "pending", datetime.datetime.now())
cursor.execute(sql, values)
mydb.commit()

donation_id = cursor.lastrowid   # Get inserted ID

# Create Razorpay order
client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))
order = client.order.create({
    "amount": int(amount * 100),   # in paise
    "currency": "INR",
    "receipt": f"donation_{donation_id}",
    "payment_capture": 1
})

# Store receipt/order_id for tracking
cursor.execute("UPDATE donations SET receipt_path=%s WHERE id=%s", (order['id'], donation_id))
mydb.commit()

# HTML – Redirect to Razorpay Checkout
print(f"""
<html>
<head><title>Processing Payment</title></head>
<body>
<script src="https://checkout.razorpay.com/v1/checkout.js"></script>
<script>
    var options = {{
        "key": "{RAZORPAY_KEY_ID}",
        "amount": "{order['amount']}",
        "currency": "INR",
        "name": "JeevanKiran NGO",
        "description": "Donation Payment",
        "order_id": "{order['id']}",
        "handler": function (response) {{
            // Call success handler
            window.location.href = "payment_success.py?donation_id={donation_id}&payment_id=" + response.razorpay_payment_id;
        }},
        "prefill": {{
            "name": "{user_name}",
            "email": "{user_email}"
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
