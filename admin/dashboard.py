#!C:/Python312/python.exe
import mysql.connector
import cgi, cgitb
from datetime import datetime, timedelta
cgitb.enable()
import header

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
cursor = db.cursor(dictionary=True)

# ===================== FETCH DONATION TOTALS =====================

def fetch_total(query):
    cursor.execute(query)
    result = cursor.fetchone()
    return result['total'] if result['total'] else 0

general_total = fetch_total("SELECT SUM(amount) AS total FROM donate_payment WHERE payment_status='PAID'")
# print(general_total)
project_total = fetch_total("SELECT SUM(amount) AS total FROM package_payment WHERE payment_status='success '")
# print(project_total)
overall_total = general_total + project_total 
# print(overall_total)

# # ===================== BIRTHDAY SECTION =====================

cursor.execute("""
    SELECT id, fullname, DateofBirth 
    FROM usersignup
    ORDER BY MONTH(DateofBirth), DAY(DateofBirth)
""")
birthdays = cursor.fetchall()
# print(birthdays)
today = datetime.now()
nearest = None

for b in birthdays:
    bday = datetime.strptime(b['DateofBirth'], "%Y-%m-%d")
    upcoming = datetime(today.year, bday.month, bday.day)
    if upcoming < today:
        upcoming = upcoming.replace(year=today.year + 1)

    if not nearest or upcoming < nearest['date']:
        nearest = {
            "id": b['id'],
            "name": b['fullname'],
            "date": upcoming
        }
# print(nearest)
# ===================== HTML =====================

print("""


<!DOCTYPE html>
<html>
<head>
<title>Dashboard</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
<style>



.dashboard {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 18px;
  margin-bottom: 30px;
}

.card {
  background: white;
  padding: 18px;
  border-radius: 12px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
  text-align: center;
}

.card h4 {
  margin-bottom: 8px;
  font-size: 17px;
  color: #333;
}

.card .value {
  font-size: 22px;
  font-weight: bold;
  color: #0d6efd;
}

.birthday-title {
  font-size: 20px;
  font-weight: bold;
  margin: 20px 0 10px 0;
}

.birthday-list table {
  width: 100%;
  border-collapse: collapse;
  background: white;
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}

.birthday-list th, .birthday-list td {
  padding: 10px;
  text-align: left;
  border-bottom: 1px solid #eee;
}

</style>
</head>
<body>

<div class='dashboard'>
""")

print(f"<div class='card'><h4>Total Donation</h4><div class='value'>₹ {overall_total}</div></div>")
print(f"<div class='card'><h4>Project Donation</h4><div class='value'>₹ {project_total}</div></div>")
print(f"<div class='card'><h4>General Donation</h4><div class='value'>₹ {general_total}</div></div>")

if nearest:
    print(f"<div class='card'><h4>Next Birthday</h4><div class='value'>{nearest['name']}<br>{nearest['date'].strftime('%d %b')}</div></div>")
else:
    print("<div class='card'><h4>Next Birthday</h4><div class='value'>No Users</div></div>")

print("""
</div>

<div class='birthday-title'>Upcoming Birthdays</div>
<div class='birthday-list'>
<table>
<thead><tr><th>ID</th><th>Name</th><th>Birthday</th></tr></thead><tbody>
""")

for b in birthdays:
    bd = datetime.strptime(b['DateofBirth'], "%Y-%m-%d")
    print(f"<tr><td>{b['id']}</td><td>{b['fullname']}</td><td>{bd.strftime('%d %b')}</td></tr>")

print("""
</tbody></table></div>
</body></html>
""")

cursor.close()
db.close()
