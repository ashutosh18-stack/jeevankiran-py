#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
print("Content-Type: text/html\n")
print('''
<html>
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Login Page</title>
  <link rel="stylesheet" href="style/login.css" />
</head>
<body>
  <div class="container">
    <div class="image-side">
      <img src="assets/adminlogin bg.jpg" alt="Teamwork" />
    </div>
    <div class="form-side fade-in">
      <div class="login-box">
        <h2>Welcome Back</h2>
        <p>Please login to continue</p>
       <form action="backend/loginbackend.py" method="post">
      <input type="text" id="phone" name="phone" placeholder="Phone Number" required />
      <input type="password" id="password"  name="password" placeholder="Password" required />
      <button type="submit">Login</button>
    </form>
        <p id="error" class="error"></p>
      </div>
    </div>
  </div>
</body>
</html>
''')