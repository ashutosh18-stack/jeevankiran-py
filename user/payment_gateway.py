#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
import json

cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
package_id = form.getvalue("package_id")

# Fetch donation details from DB
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
cursor = mydb.cursor(dictionary=True)

cursor.execute("SELECT * FROM package_donations WHERE id = %s", (package_id,))
donation = cursor.fetchone()

if not donation:
    print("<h3>Invalid Donation ID</h3>")
    exit()

# Razorpay Test Key
RAZORPAY_KEY_ID = "rzp_test_Ljv38fH05BvsXL"
amount_in_paise = int(float(donation["amount"]) * 100)  # Razorpay uses paise

# Razorpay HTML Checkout Integration
print(f"""
<html>
  <head>
    <title>Payment Gateway</title>
    <script src="https://checkout.razorpay.com/v1/checkout.js"></script>
  </head>
  <body>
    <h2>Processing Donation: #{donation['id']}</h2>
    <p>Amount: RS.{donation['amount']}</p>
    <button id="rzp-button1">Pay with Razorpay</button>

    <script>
      var options = {{
          "key": "{RAZORPAY_KEY_ID}",
          "amount": "{amount_in_paise}",
          "currency": "INR",
          "name": "Jeevankiran Donation",
          "description": "Donation for package ID: {donation['package_id']}",
          "handler": function (response){{
              alert("Payment Successful! Razorpay ID: " + response.razorpay_payment_id);
              window.location.href = "backend/payment_success_backend.py?package_id={package_id}&payment_id=" + response.razorpay_payment_id;
          }},
          "prefill": {{
              "name": "Donor",
              "email": "{donation['user_email'] or ''}"
          }},
          "theme": {{
              "color": "#3399cc"
          }}
      }};
      var rzp1 = new Razorpay(options);
      document.getElementById('rzp-button1').onclick = function(e){{
          rzp1.open();
          e.preventDefault();
      }}
    </script>
  </body>
</html>
""")
