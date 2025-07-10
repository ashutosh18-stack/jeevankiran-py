#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
print("Content-Type: text/html\n")
print('''
      <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Welcome Admin - Jeevan Kiran</title>
<link rel="stylesheet" href="style/main.css">
</head>
<body>
  <div class="container" id="welcomeContainer">
    <div class="ngo-title">Jeevan Kiran</div>
    <button class="welcome-button" id="welcomeBtn">Welcome Admin</button>
  </div>

  <script>
    const btn = document.getElementById('welcomeBtn');
    const container = document.getElementById('welcomeContainer');

    btn.addEventListener('click', () => {
      container.classList.add('slide-up');
      setTimeout(() => {
        window.location.href = "login.py"; 
      }, 1000);
    });
  </script>
</body>
</html>
''')