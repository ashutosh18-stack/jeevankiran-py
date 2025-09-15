#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
import header


form = cgi.FieldStorage()
admin_id = form.getvalue("admin_id")
print(f'''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>NGO Master Menu</title>
  <link rel="stylesheet" href="style/ngomaster.css" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" />
</head>
<body>
  <div class="dashboard-container">
    <h1><i class="fas fa-hands-helping"></i> NGO Master Panel</h1>
    
    <div class="card-wrapper">
      <!-- Add NGO -->
      <div class="card" onclick="goTo('ngocreate.py?admin_id={admin_id}')">
        <i class="fas fa-plus-circle icon"></i>
        <h2>Add NGO</h2>
        <p>Create a new NGO entry with full details</p>
      </div>

      <!-- NGO List -->
      <div class="card" onclick="goTo('ngomasterlist.py?admin_id={admin_id}')">
        <i class="fas fa-list icon"></i>
        <h2>NGO List</h2>
        <p>View, edit or delete NGOs from the system</p>
      </div>
    </div>
  </div>
''')
print('''
  <script>
    function goTo(page) {
      window.location.href = page;
    }
  </script>
</body>
</html>
''')
