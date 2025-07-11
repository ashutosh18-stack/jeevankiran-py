#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
import header

# Dummy data (replace with database values)
total_projects = 12
total_donors = 58
total_donations = 453250

recent_donations = [
    {"name": "Ravi Kumar", "project": "Food Drive", "amount": 2000},
    {"name": "Anita Shah", "project": "School Kit", "amount": 1500},
    {"name": "Rahul Mehta", "project": "Medical Camp", "amount": 3000}
]

special_campaigns = [
    {"title": "Winter Blanket Drive", "status": "Active"},
    {"title": "Child Health Camp", "status": "Completed"}
]

donor_birthdays = [
    {"name": "Neha Joshi", "phone": "9876543210", "email": "neha@example.com"},
    {"name": "Arjun Reddy", "phone": "9876540000", "email": "arjun@example.com"}
]

print('''
  <head>
    <link rel="stylesheet" href="style/dashboard.css">
  </head>

  <h2><i class="fas fa-home"></i> Dashboard (Home)</h2>

  <div class="dashboard-cards">
    <div class="card">
      <h3>Total Projects</h3>
      <p>''' + str(total_projects) + '''</p>
    </div>

    <div class="card">
      <h3>Total Donors</h3>
      <p>''' + str(total_donors) + '''</p>
    </div>

    <div class="card">
      <h3>Total Donations</h3>
      <p>₹ ''' + str(total_donations) + '''</p>
    </div>
  </div>

  <div class="section">
    <h3>Recent Donations</h3>
    <table>
      <thead>
        <tr><th>Donor</th><th>Project</th><th>Amount (₹)</th></tr>
      </thead>
      <tbody>''')

for donation in recent_donations:
    print(f"<tr><td>{donation['name']}</td><td>{donation['project']}</td><td>{donation['amount']}</td></tr>")

print('''
      </tbody>
    </table>
  </div>

  <div class="section">
    <h3>Special Campaigns</h3>
    <ul class="campaign-list">''')

for campaign in special_campaigns:
    status_class = "active" if campaign['status'] == "Active" else "completed"
    print(f'<li class="{status_class}">{campaign["title"]} - {campaign["status"]}</li>')

print('''
    </ul>
  </div>

  <div class="section">
    <h3>Donor Birthdays Today</h3>
    <ul class="birthday-list">''')

for donor in donor_birthdays:
    print(f'''
      <li>
        <strong>{donor["name"]}</strong>
        <a href="tel:{donor["phone"]}" class="contact-btn">📞</a>
        <a href="mailto:{donor["email"]}" class="contact-btn">✉️</a>
      </li>
    ''')

print('''
    </ul>
  </div>

</div>
</div>
</body>
</html>
''')
