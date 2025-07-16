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
  <title>Sign Up - Charity Website</title>
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <link rel="stylesheet" href="css/bootstrap.min.css">
  <link rel="stylesheet" href="css/style.css">
  <style>
    body {
      background-color: #f8f9fa;
    }
    .signup-form {
      max-width: 500px;
      margin: 50px auto;
      padding: 30px;
      background-color: #fff;
      box-shadow: 0 0 15px rgba(0,0,0,0.1);
      border-radius: 8px;
    }
    .signup-form h2 {
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

<div class="signup-form">
  <h2>Create Your Account</h2>
  <form action="signupbackend.py" method="post">
    <div class="form-group">
      <label for="name">Full Name</label>
      <input type="text" class="form-control" id="fullname" name="fullname" required>
    </div>
    <div class="form-group">
      <label for="email">Email address</label>
      <input type="email" class="form-control" id="email" name="email" required>
    </div>
    <div class="form-group">
      <label for="phone">Phone Number</label>
      <input type="tel" class="form-control" id="phonenumber" name="phonenumber" required>
    </div>
    <div class="form-group">
      <label for="dob">Date of Birth</label>
      <input type="date" class="form-control" id="DateofBirth" name="DateofBirth" required>
    </div>
    <div class="form-group">
      <label for="password">Password</label>
      <input type="password" class="form-control" id="password" name="password" required>
    </div>
    <div class="form-group">
      <label for="confirm_password">Confirm Password</label>
      <input type="password" class="form-control" id="confirm_password" name="confirm_password" required>
    </div>
    <div class="form-group text-center">
      <button type="submit" class="btn btn-primary btn-block">Sign Up</button>
    </div>
  </form>
  <p class="text-center mt-3">Already have an account? <a href="login.py">Log in here</a></p>
</div>

<script src="js/jquery.min.js"></script>
<script src="js/bootstrap.min.js"></script>
</body>
</html>
''')

