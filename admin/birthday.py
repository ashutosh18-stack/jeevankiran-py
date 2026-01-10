#!C:/Python312/python.exe
import cgi, cgitb
cgitb.enable()
import header
import mysql.connector
from datetime import datetime


# ==== DB CONNECT ====
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
cur = db.cursor(dictionary=True)

cur.execute("SELECT id, fullname, DateofBirth FROM usersignup")
users = cur.fetchall()

today = datetime.today()
current_month = today.month

processed = []

# Convert DOB + extract month/day
for u in users:
    try:
        dob = datetime.strptime(str(u["DateofBirth"]), "%Y-%m-%d")
    except:
        continue  # skip invalid DOB format

    u["month"] = dob.month
    u["day"] = dob.day
    u["dob_str"] = dob.strftime("%d %b")
    processed.append(u)

# SORT BY upcoming birthdays
sorted_users = sorted(processed, key=lambda x: (x["month"], x["day"]))

# FILTER for cards
this_month = [u for u in sorted_users if u["month"] == current_month]
upcoming = [u for u in sorted_users if u["month"] > current_month] + \
           [u for u in sorted_users if u["month"] < current_month]

card1 = this_month[0] if this_month else None
card2 = upcoming[0] if upcoming else None
card3 = upcoming[1] if len(upcoming) > 1 else None

# ==== HTML OUTPUT WITH DESIGN ====
print("""
<!DOCTYPE html>
<html>
<head>
<title>Birthdays</title>
<style>
 
.section-title{
    font-size:24px;
    font-weight:bold;
    margin-bottom:15px;
}
.card-container{
    display:flex;
    gap:20px;
    margin-bottom:40px;
}
.card{
    width:30%;
    background:white;
    padding:20px;
    border-radius:10px;
    box-shadow:0 3px 10px rgba(0,0,0,0.1);
}
.card h3{
    margin:0;
    margin-bottom:10px;
    color:#2c7a7b;
}
.table-container{
    background:white;
    padding:20px;
    border-radius:10px;
    box-shadow:0 3px 10px rgba(0,0,0,0.1);
}
table{
    width:100%;
    border-collapse:collapse;
}
th, td{
    padding:10px;
    border-bottom:1px solid #ddd;
    text-align:left;
}
th{
    background:#2c7a7b;
    color:white;
}
</style>
</head>
<body>
<h2 class='section-title'>Upcoming Birthdays</h2>
<div class='card-container'>
""")

def card(title, data):
    if data:
        print(f"""
        <div class='card'>
            <h3>{title}</h3>
            <p><b>ID:</b> {data['id']}</p>
            <p><b>Name:</b> {data['fullname']}</p>
            <p><b>Birthday:</b> {data['dob_str']}</p>
        </div>
        """)
    else:
        print(f"""
        <div class='card'>
            <h3>{title}</h3>
            <p>No record</p>
        </div>
        """)

# Print cards
card("Birthday This Month", card1)
card("Next Birthday", card2)
card("Next After That", card3)

print("</div>")

# LIST TABLE
print("""
<div class='table-container'>
<h2 class='section-title'>Birthday List (Sorted)</h2>
<table>
<thead>
<tr>
<th>ID</th>
<th>Name</th>
<th>Birthday</th>
</tr>
</thead>
<tbody>
""")

for u in sorted_users:
    print(f"""
    <tr>
        <td>{u['id']}</td>
        <td>{u['fullname']}</td>
        <td>{u['dob_str']}</td>
    </tr>
    """)

print("""
</tbody>
</table>
</div>
</body>
</html>
""")
