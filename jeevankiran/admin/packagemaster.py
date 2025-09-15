#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
import header

print('''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>NGO Master Menu</title>
  <link rel="stylesheet" href="style/projectmaster.css" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" />
</head>
<body>
  <div class="dashboard-container">
    <h1><i class="fas fa-hands-helping"></i> Package Master Panel</h1>
    
    <div class="card-wrapper">
      <!-- Add NGO -->
      <div class="card" onclick="goTo('packagecreate.py')">
        <i class="fas fa-plus-circle icon"></i>
        <h2>Add Packages</h2>
        <p>Create a new Packages entry with full details</p>
      </div>

      <!-- NGO List -->
      <div class="card" onclick="goTo('packagelist.py')">
        <i class="fas fa-list icon"></i>
        <h2>Package List</h2>
        <p>View, edit or delete Package from the system</p>
      </div>
    </div>
  </div>

  <script>
    function goTo(page) {
      window.location.href = page;
    }
  </script>
</body>
</html>
''')
