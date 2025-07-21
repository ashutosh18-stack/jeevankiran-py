#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()

print("Content-Type: text/html\n")
form = cgi.FieldStorage()
admin_id = form.getvalue("admin_id")

print(f'''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Admin Panel</title>
  <link rel="stylesheet" href="style/header.css" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
</head>
<body>

<div class="container">
  <!-- Sidebar -->
  <aside id="sidebar" class="sidebar collapsed">
    <div class="logo">
      <a href="dashboard.py"><i class="fas fa-hands-helping"></i><span class="logo-text"> NGO Panel</span></a>
    </div>
    <nav class="nav">
      <ul>
        <li><a href="dashboard.py?admin_id={admin_id}"><i class="fas fa-tachometer-alt"></i><span>Dashboard</span></a></li>
        <li><a href="ngomaster.py?admin_id={admin_id}"><i class="fas fa-building"></i><span>NGO Master</span></a></li>
        <li><a href="projectmaster.py?admin_id={admin_id}"><i class="fas fa-project-diagram"></i><span>Project Master</span></a></li>
        <li><a href="packagemaster.py?admin_id={admin_id}"><i class="fas fa-box"></i><span>Package Master</span></a></li>
        <li><a href="#"><i class="fas fa-hand-holding-heart"></i><span>Donation Master</span></a></li>
        <li><a href="#"><i class="fas fa-bullhorn"></i><span>Special Campaigns</span></a></li>
        <li><a href="volunteermaster.py"><i class="fa-solid fa-hands-holding-child"></i><span>Volunteer</span></a></li>
        <li><a href="feedbackmaster.py"><i class="fa-solid fa-comments"></i><span>Feedback</span></a></li>
        <li><a href="donormaster.py"><i class="fas fa-user-friends"></i><span>Donors</span></a></li>
        <li><a href="#"><i class="fas fa-receipt"></i><span>Receipts</span></a></li>
        <li><a href="#"><i class="fas fa-birthday-cake"></i><span>Birthdays</span></a></li>
      </ul>
    </nav>
  </aside>

  <!-- Main content -->
  <div class="main">
    <header class="header">
      <button id="toggleBtn" class="menu-btn"><i class="fas fa-bars"></i></button>
      <div class="admin-dropdown">
        <button class="admin-btn">Admin <i class="fas fa-caret-down"></i></button>
        <div class="dropdown-content">
          <a href="myprofile.py?admin_id={admin_id}">My Profile</a>
          <a href="logout.py">Logout</a>
        </div>
      </div>
    </header>

    <div class="content"> <!-- page-specific content starts here -->
''')
print(''' 
<script>
  const toggleBtn = document.getElementById("toggleBtn");
  const sidebar = document.getElementById("sidebar");

  toggleBtn.addEventListener("click", () => {
    sidebar.classList.toggle("collapsed");
  });
</script>
''')
