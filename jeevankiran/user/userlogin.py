#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
print("Content-Type: text/html\n")
print('''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Login - Charity Website</title>
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <link rel="stylesheet" href="css/bootstrap.min.css">
  <link rel="stylesheet" href="css/style.css">
  <style>
    body {
      background-color: #f8f9fa;
    }
    .login-form {
      max-width: 400px;
      margin: 50px auto;
      padding: 30px;
      background-color: #fff;
      box-shadow: 0 0 15px rgba(0,0,0,0.1);
      border-radius: 8px;
    }
    .login-form h2 {
      text-align: center;
      margin-bottom: 20px;
      color: #007bff;
    }
    .btn-primary {
      background-color: #007bff;
      border: none;
    }
  </style>
</head>
<body>

<div class="login-form">
  <h2>Login to Your Account</h2>
  <form action="backend/userloginbackend.py" method="post">
    <div class="form-group">
      <label for="phone">Phone Number</label>
      <input type="tel" class="form-control" id="phonenumber" name="phonenumber" required>
    </div>
    <div class="form-group">
      <label for="password">Password</label>
      <input type="password" class="form-control" id="password" name="password" required>
    </div>
    <div class="form-group text-center">
      <button type="submit" class="btn btn-primary btn-block">Login</button>
    </div>
  </form>
  <p class="text-center mt-3">Don't have an account? <a href="signup.py">Sign up here</a></p>
</div>

<script src="js/jquery.min.js"></script>
<script src="js/bootstrap.min.js"></script>
</body>
</html>
''')
