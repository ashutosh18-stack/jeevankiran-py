#!C:\Python312\python.exe
import cgi, cgitb, os, mysql.connector, html
cgitb.enable()

form = cgi.FieldStorage()
sid = form.getfirst("sid")

if not sid:
    print("Content-Type: text/html\n")
    print("<h2 style='color:red; text-align:center;'>Session expired. Please login again.</h2>")
    exit()

# Session check
session_file = os.path.join(os.path.dirname(__file__), "sessions", f"{sid}.txt")
if not os.path.exists(session_file):
    print("Content-Type: text/html\n")
    print("<h2 style='color:red; text-align:center;'>Invalid session. Please login again.</h2>")
    exit()

with open(session_file) as f:
    user_id = f.read().strip()

# Database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
cursor = mydb.cursor(dictionary=True)
cursor.execute("""
    SELECT * FROM package_payment 
    WHERE payment_status='success' AND user_id=%s
    ORDER BY payment_date DESC
""", (user_id,))
donations = cursor.fetchall()

# HTML start
print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>My Paid Receipts</title>
<style>
body { font-family: Arial, sans-serif; background:#f5f5f5; padding:0; margin:0; }
header { position: fixed; top:0; width:100%; z-index:100; }
.content { padding-top:80px; } /* space for fixed header */
table { width:90%; border-collapse: collapse; margin:20px auto; background:white; }
th, td { padding:12px; border:1px solid #ddd; text-align:center; }
th { background:orange; color:black; }
tr:nth-child(even) { background:#f9f9f9; }
.btn { background:#28a745; color:white; padding:6px 12px; text-decoration:none; border-radius:5px; font-size:14px; }
.btn:hover { background:#fd7e14; }
.back { margin:20px auto; text-align:center; }
.back a { color:#007bff; text-decoration:none; font-weight:bold; }
.back a:hover { text-decoration:underline; }
h2 { text-align:center; margin-top:0; padding-top:0; }

/* Back arrow at top-left */
.top-back {
    position: fixed;
    top: 50px;
    left: 70px;
    font-size: 50px;
    text-decoration: none;
    color:#fd7e14;
    font-weight: 800;
    z-index: 101;
}
.top-back:hover { color: #0056b3; }
</style>
</head>
<body>
""")

# Back arrow link (top-left)
print(f"<a href='index.py?id={sid}' class='top-back'>&larr; </a>")

# Page content
print("<div class='content'>")  # content below fixed header
print("<h2>My Paid Receipts</h2>")
print("<table><tr><th>Name</th><th>Email</th><th>Package Item</th><th>Qty</th><th>Amount</th><th>Payment Date</th><th>Transaction ID</th><th>Action</th></tr>")

if donations:
    for d in donations:
        name = html.escape(d.get('user_name',''))
        email = html.escape(d.get('user_email',''))
        item = html.escape(d.get('package_item',''))
        qty = d.get('quantity',0)
        amount = float(d.get('amount') or 0)
        date = d.get('payment_date')
        date = date.strftime("%Y-%m-%d %H:%M:%S") if date else "N/A"
        txn = html.escape(d.get('transaction_id',''))
        donation_id = d.get('donated_id')

        print(f"<tr><td>{name}</td><td>{email}</td><td>{item}</td><td>{qty}</td><td>INR {amount:.2f}</td><td>{date}</td><td>{txn}</td><td><a href='backend/receipt_pdf.py?donation_id={donation_id}&sid={sid}' class='btn'>Download Now</a></td></tr>")
else:
    print("<tr><td colspan='8'>No paid receipts found for your account.</td></tr>")

print(f"</table><div class='back'><a href='index.py?sid={sid}'>← Back to Dashboard</a></div></div></body></html>")
