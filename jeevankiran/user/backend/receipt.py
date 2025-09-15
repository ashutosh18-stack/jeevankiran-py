#!C:\Python312\python.exe
import cgi, cgitb
cgitb.enable()
import mysql.connector
import sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print("Content-Type: text/html; charset=utf-8\n")

form = cgi.FieldStorage()
donation_id = form.getvalue("donated_id")

if not donation_id:
    print("<h2>No Donation ID provided!</h2>")
    exit()

mydb = mysql.connector.connect(
    host="localhost", user="root", password="", database="jeevankiran"
)
cursor = mydb.cursor(dictionary=True)
cursor.execute("SELECT * FROM package_payment WHERE donated_id=%s", (donation_id,))
donation = cursor.fetchone()

if not donation:
    print("<h2>Invalid Donation ID</h2>")
    exit()

# --- Receipt UI ---
print(f"""
<!DOCTYPE html>
<html>
<head>
    <title>Donation Receipt</title>
    <style>
        body {{ font-family: Arial, sans-serif; background:#f5f5f5; }}
        .receipt {{
            width: 600px; margin: 40px auto; padding: 30px;
            background: white; border: 1px solid #ddd; border-radius: 8px;
        }}
        h2 {{ text-align: center; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
        td {{ padding: 10px; border-bottom: 1px solid #eee; }}
        td.label {{ font-weight: bold; width: 40%; }}
        .actions {{ margin-top: 20px; text-align:center; }}
        .btn {{ background:#007bff; color:white; padding:10px 20px; text-decoration:none; border-radius:5px; margin:5px; display:inline-block; }}
        .btn:hover {{ background:#0056b3; }}
        .btn-close {{ background:#dc3545; }}
        .btn-close:hover {{ background:#a71d2a; }}
        .btn-index {{ background:#28a745; }}
        .btn-index:hover {{ background:#1c7c31; }}
    </style>
    <script>
        function closeWindow() {{
            window.close();
        }}
    </script>
</head>
<body>
    <div class="receipt">
        <h2>Donation Receipt</h2>
        <table>
            <tr><td class="label">Receipt No.</td><td>{donation['donated_id']}</td></tr>
            <tr><td class="label">Name</td><td>{donation['user_name']}</td></tr>
            <tr><td class="label">Email</td><td>{donation['user_email']}</td></tr>
            <tr><td class="label">Package Item</td><td>{donation['package_item']}</td></tr>
            <tr><td class="label">Quantity</td><td>{donation['quantity']}</td></tr>
            <tr><td class="label">Amount</td><td>INR {donation['amount']}</td></tr>
            <tr><td class="label">Payment Status</td><td>{donation['payment_status']}</td></tr>
            <tr><td class="label">Payment Date</td><td>{donation['payment_date']}</td></tr>
            <tr><td class="label">Transaction ID</td><td>{donation['transaction_id']}</td></tr>
        </table>
        <div class="actions">
            <a href="receipt_pdf.py?donation_id={donation['donated_id']}" class="btn">Download PDF</a>
            <a href="../index.py?id={donation['user_id']}" class="btn btn-index">Back to Home</a>
        
        </div>
    </div>
</body>
</html>
""")
