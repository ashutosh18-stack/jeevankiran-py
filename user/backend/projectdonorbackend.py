#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
import mysql.connector
import sys, io

# Ensure UTF-8 output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Content-Type: text/html; charset=utf-8\n")

form = cgi.FieldStorage()

# Collect form values
user_id = form.getvalue("userid")
user_name = form.getvalue("name")
user_email = form.getvalue("email")
package_id = form.getvalue("package_id")
package_item = form.getvalue("item")
quantity = form.getvalue("quantity")
amount = form.getvalue("amount")
message = form.getvalue("message")

# Connect to database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
cursor = mydb.cursor()

# Insert into package_payment table
sql = """INSERT INTO package_payment
(user_id, user_name, user_email, package_id, package_item, quantity, amount, message, payment_status)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, 'pending')"""

values = (user_id, user_name, user_email, package_id, package_item, quantity, amount, message)
cursor.execute(sql, values)
mydb.commit()

donated_id = cursor.lastrowid  # Newly inserted record ID

# --- UI Section ---
print(f"""
<!DOCTYPE html>
<html>
<head>
    <title>Donation Confirmation</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background: #f9f9f9;
            margin: 0;
            padding: 0;
        }}
        .container {{
            max-width: 600px;
            margin: 60px auto;
            background: #ffffff;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            text-align: center;
        }}
        h2 {{
            color: #333;
            margin-bottom: 20px;
        }}
        table {{
            width: 100%;
            margin: 20px 0;
            border-collapse: collapse;
        }}
        td {{
            padding: 12px;
            border-bottom: 1px solid #eee;
            text-align: left;
            font-size: 16px;
        }}
        td.label {{
            font-weight: bold;
            color: #555;
            width: 40%;
        }}
        .btn {{
            display: inline-block;
            padding: 12px 24px;
            background: #007bff;
            color: #fff;
            text-decoration: none;
            border-radius: 6px;
            font-size: 16px;
            transition: background 0.3s ease;
        }}
        .btn:hover {{
            background: #0056b3;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h2>Donation Request Saved</h2>
        <p>Your donation request has been recorded successfully.</p>
        <table>
            <tr><td class="label">Donation ID</td><td>{donated_id}</td></tr>
            <tr><td class="label">Name</td><td>{user_name}</td></tr>
            <tr><td class="label">Email</td><td>{user_email}</td></tr>
            <tr><td class="label">Package Item</td><td>{package_item}</td></tr>
            <tr><td class="label">Quantity</td><td>{quantity}</td></tr>
            <tr><td class="label">Amount</td><td>INR {amount}</td></tr>
        </table>
       <form action="paymentgateway.py?donated_id={donated_id}" method="post">
    <input type="hidden" name="donated_id" value="{donated_id}">
    <button type="submit" class="btn">Go to Payment</button>
</form>
    </div>
</body>
</html>
""")
