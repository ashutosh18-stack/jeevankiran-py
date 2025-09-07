#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
import mysql.connector
import sys, io, traceback, html

# Ensure UTF-8 output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
print("Content-Type: text/html; charset=utf-8\n")

# ---------- Configuration ----------
RAZORPAY_KEY_ID = "rzp_test_RDxnTJFjtdr936"
RAZORPAY_KEY_SECRET = "1zg6Nmrq4VcVmJK5SOAI7uTz"

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "jeevankiran"
}
# -----------------------------------

def show_error(msg):
    print(f"<h3 style='color:red;font-family:Arial'>{html.escape(msg)}</h3>")
    sys.exit(1)

try:
    import razorpay
except:
    show_error("Install razorpay module: pip install razorpay")

form = cgi.FieldStorage()
donated_id = form.getfirst("donated_id") or form.getfirst("donation_id")
if not donated_id:
    show_error("Missing donated_id")

# If multiple values came, pick first
donated_id = str(donated_id).strip()

db = mysql.connector.connect(**DB_CONFIG)
cursor = db.cursor()

cursor.execute("SELECT amount, user_email, user_name FROM package_payment WHERE donated_id=%s", (donated_id,))
row = cursor.fetchone()
if not row:
    cursor.execute("SELECT amount, user_email, user_name FROM package_payment WHERE id=%s", (donated_id,))
    row = cursor.fetchone()
if not row:
    show_error(f"No donation record found for ID {donated_id}")

amount_str, email, name = row
amount_paise = int(float(amount_str) * 100)

client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))
order = client.order.create({"amount": amount_paise, "currency": "INR", "payment_capture": 1})
razor_order_id = order["id"]

# Save order id in DB
cursor.execute("UPDATE package_payment SET 	razorpay_order_id=%s WHERE donated_id=%s", (razor_order_id, donated_id))
if cursor.rowcount == 0:
    cursor.execute("UPDATE package_payment SET 	razorpay_order_id=%s WHERE id=%s", (razor_order_id, donated_id))
db.commit()

# Escape values
name_safe = html.escape(name or "")
email_safe = html.escape(email or "")
donated_id_safe = html.escape(donated_id)

# ---------------- HTML Output ----------------
print(f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Redirecting to Payment...</title>
</head>
<body>
  <script src="https://checkout.razorpay.com/v1/checkout.js"></script>
  <script>
    var options = {{
        "key": "{RAZORPAY_KEY_ID}",
        "amount": "{amount_paise}",
        "currency": "INR",
        "name": "NGO Donation",
        "description": "Donation Payment",
        "order_id": "{razor_order_id}",
        "prefill": {{
            "name": "{name_safe}",
            "email": "{email_safe}"
        }},
        "handler": function (response) {{
            // Redirect to status page after success
            var f = document.createElement('form');
            f.method = 'POST';
            f.action = 'paymentstatus.py';

            var i1 = document.createElement('input');
            i1.type='hidden'; i1.name='donated_id'; i1.value="{donated_id_safe}";

            var i2 = document.createElement('input');
            i2.type='hidden'; i2.name='razorpay_payment_id'; i2.value=response.razorpay_payment_id;

            var i3 = document.createElement('input');
            i3.type='hidden'; i3.name='razorpay_order_id'; i3.value=response.razorpay_order_id;

            var i4 = document.createElement('input');
            i4.type='hidden'; i4.name='razorpay_signature'; i4.value=response.razorpay_signature;

            f.appendChild(i1); f.appendChild(i2); f.appendChild(i3); f.appendChild(i4);
            document.body.appendChild(f);
            f.submit();
        }}
    }};
    var rzp1 = new Razorpay(options);
    rzp1.open();   // auto open Razorpay checkout
  </script>
</body>
</html>""")
