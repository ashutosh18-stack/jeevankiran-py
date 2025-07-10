#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
import mysql.connector
print("Context-Type:text/html\n")
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="jeevankiran")
mycursor=mydb.cursor()
query =f'''SELECT * FROM adminlogin'''
# print(query)
mycursor.execute(query)
result=mycursor.fetchall()
print('''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Admin Panel</title>
  <link rel="stylesheet" href="style/style.css" />
  <script defer src="js/script.js"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" />
</head>
<body>
  <div class="container">
    <!-- Sidebar -->
      <aside class="sidebar">
      <a href="index.html"><div class="logo">NGO Panel</div></a>
      <nav class="sidebar-nav">
        <a href="dashboard.html"><i class="fa-solid fa-chart-line"></i> Dashboard</a>
        <a href="#"><i class="fa-solid fa-building"></i> NGO Master</a>
        <a href="#"><i class="fa-solid fa-folder-open"></i> Project Master</a>
        <a href="#"><i class="fa-solid fa-box-open"></i> Package Master</a>
        <a href="#"><i class="fa-solid fa-hand-holding-dollar"></i> Donation Master</a>
        <a href="#"><i class="fa-solid fa-bullseye"></i> Special Campaigns</a>
        <a href="#"><i class="fa-solid fa-user-group"></i> Donors</a>
        <a href="#"><i class="fa-solid fa-file-invoice-dollar"></i> Receipts</a>
        <a href="#"><i class="fa-solid fa-cake-candles"></i> Birthdays</a>
        <a href="#"><i class="fa-solid fa-right-from-bracket"></i> Logout</a>
      </nav>
    </aside>

    <!-- Main content area -->
    <div class="main">
      <!-- Top navbar -->
      <header class="topbar">
        <div class="admin-profile">
          <div class="profile-icon" id="dropdownToggle">
            <i class="fas fa-user-circle"></i>
            
            <span>Admin</span> 
            
            
            <i class="fas fa-caret-down"></i>
            
          </div>
''')
for x in result:

    print(f'''
          <div class="dropdown" id="dropdownMenu">
            <a href="myprofile.py?admin_id={x[0]}">My Profile</a>
            <a href="logout.py">Logout</a>
          </div>
          ''')
print('''
        </div>
      </header>
''')