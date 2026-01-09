#!C:/Python312/python.exe
import cgi
import cgitb
cgitb.enable()

import mysql.connector
import sys, io

# UTF-8 output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Content-Type: text/html; charset=utf-8\n")

form = cgi.FieldStorage()
donation_id = form.getvalue("donation_id")

# Validation
if not donation_id:
    print("<h2>Donation ID missing</h2>")
    print("<p>Please start donation again.</p>")
    sys.exit()

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="jeevankiran"
    )

    cursor = mydb.cursor(dictionary=True)

    cursor.execute(
        "SELECT donation_id, name, email, amount FROM donate_payment WHERE donation_id=%s",
        (donation_id,)
    )

    donation = cursor.fetchone()

    cursor.close()
    mydb.close()

    if not donation:
        print("<h2>Invalid Donation ID</h2>")
        sys.exit()

except Exception as e:
    print("<h3>Database Error</h3>")
    print("<pre>", e, "</pre>")
    sys.exit()

print(f"""
<!DOCTYPE html>
<html>
<head>
    <title>Donation Confirmation</title>
    <meta charset="utf-8">
    <style>
        body {{
            background:#f4f6f8;
            font-family: Arial;
        }}
        .box {{
            width:450px;
            margin:80px auto;
            background:white;
            padding:25px;
            border-radius:8px;
            box-shadow:0 0 10px #ccc;
        }}
        .row {{
            margin-bottom:10px;
        }}
        .label {{
            font-weight:bold;
        }}
        .btn {{
            padding:10px 20px;
            text-decoration:none;
            border-radius:5px;
            color:white;
        }}
        .confirm {{ background:#28a745; }}
        .cancel {{ background:#dc3545; }}
    </style>
</head>
<body>

<div class="box">
    <h2 align="center">Confirm Donation</h2>

    <div class="row"><span class="label">Donation ID:</span> {donation['donation_id']}</div>
    <div class="row"><span class="label">Name:</span> {donation['name']}</div>
    <div class="row"><span class="label">Email:</span> {donation['email']}</div>
    <div class="row"><span class="label">Amount:</span> ₹ {donation['amount']}</div>

    <hr>

    <form action="donation_gateway.py" method="post">
        <input type="hidden" name="donation_id" value="{donation['donation_id']}">
        <button class="btn confirm" type="submit">Confirm</button>
        <a href="donation_cancel.py?donation_id={donation['donation_id']}" class="btn cancel">Cancel</a>
    </form>
</div>

</body>
</html>
""")
