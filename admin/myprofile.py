#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
import mysql.connector
print("Content-Type: text/html\n")
form = cgi.FieldStorage()
admin_id = form.getvalue("admin_id")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
mycursor = mydb.cursor()
query = f"SELECT * FROM adminlogin WHERE admin_id='{admin_id}'"
mycursor.execute(query)
myresult = mycursor.fetchone()
print('''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Edit Profile</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
  <link rel="stylesheet" href="style/myprofile.css">

</head>
<body>
  <div class="page-container">
    <header>
      <div class="back-arrow" onclick="history.back()">
        <i class="fas fa-arrow-left"></i>
      </div>
      <div class="page-title">Edit Profile</div>
''')

if str(admin_id) == "1":
    print('''
      <a href="newadmin.py?admin_id=1" style="text-decoration: none;" class="add-admin-btn">+ Add New Admin</a>
    ''')
print('''
    </header>
''')

print(f'''
<main><form action="backend/profileupdate.py" method="post" enctype="multipart/form-data" onsubmit="return validateForm()">

    <!-- Section 1: Profile Image -->
    <section class="section image-section">
      <div class="profile-image-wrapper">
        <label for="imageUpload" class="image-container" id="imageContainer">
          <i class="fas fa-plus icon-plus" id="plusIcon"></i>
          <img id="profileImagePreview" src="" alt="Profile" hidden>
        </label>
        <input type="file" id="imageUpload" name="profile_image" accept="image/*" hidden>
        <button id="doneButton" class="done-btn" hidden>Done</button>
      </div>
    </section>

    <!-- Section 2: Name -->
    <section class="section name-section">
      <div class="input-group">
        <label>Admin ID</label>
        <input type="text" name="admin_id" value="{myresult[0]}" readonly />
      </div>
      <div class="input-group">
        <label>First Name</label>
        <input type="text" name="first_name" value="{myresult[1]}" placeholder="Enter first name">
      </div>
      <div class="input-group">
        <label>Middle Name</label>
        <input type="text" name="middle_name" value="{myresult[2]}" placeholder="Enter middle name">
      </div>
      <div class="input-group">
        <label>Last Name</label>
        <input type="text" name="last_name" value="{myresult[3]}" placeholder="Enter last name">
      </div>
    </section>

    <!-- Section 3: Address -->
    <section class="section">
      <div class="input-group full-width">
        <label>Address</label>
        <input type="text" name="address" value="{myresult[4]}" placeholder="Enter your address">
      </div>
    </section>

    <!-- Section 4: Email & Phone -->
    <section class="section">
      <div class="input-group">
        <label>Email</label>
        <input type="email" name="email" value="{myresult[5]}" placeholder="Enter email">
      </div>
      <div class="input-group">
        <label>Confirm Email</label>
        <input type="email" name="confirm_email" value="{myresult[5]}" placeholder="Confirm email">
      </div>
       <div class="input-group">
        <label>Date of Birth</label>
        <input type="date" name="dob" value="{myresult[6]}" required>
      </div>
      <div class="input-group full-width">
        <label>Phone Number</label>
        <input type="tel" name="phone" value="{myresult[7]}" placeholder="Enter phone number">
      </div>
    </section>

    <!-- Section 5: Password -->
    <section class="section">
<div class="input-group full-width password-wrapper">
  <label>New Password</label>
  <div class="password-input">
    <input type="password" id="newPass" name="new_password" value="{myresult[8]}" placeholder="Enter new password">
    <i class="fas fa-eye toggle-password" onclick="togglePassword('newPass', this)"></i>
  </div>
</div>

<div class="input-group full-width password-wrapper">
  <label>Confirm Password</label>
  <div class="password-input">
    <input type="password" id="confirmPass" name="confirm_password" value="{myresult[8]}" placeholder="Confirm new password">
    <i class="fas fa-eye toggle-password" onclick="togglePassword('confirmPass', this)"></i>
  </div>
</div>
      
    </section>

    <!-- Section 6: Save -->
    <section class="section">
      <div class="input-group full-width">
        <button type="submit" class="save-btn">Save Changes</button>
      </div>
    </section>
  </form>
</main>
''')

print('''
</div>

<script>
  const imageUpload = document.getElementById('imageUpload');
  const profileImagePreview = document.getElementById('profileImagePreview');
  const plusIcon = document.getElementById('plusIcon');
  const doneButton = document.getElementById('doneButton');

  imageUpload.addEventListener('change', function () {
    const file = this.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function (e) {
        profileImagePreview.src = e.target.result;
        profileImagePreview.removeAttribute('hidden');
        plusIcon.style.display = 'none';
        doneButton.removeAttribute('hidden');
      };
      reader.readAsDataURL(file);
    }
  });

  doneButton.addEventListener('click', () => {
    doneButton.setAttribute('hidden', true);
  });

  function togglePassword(inputId, iconElement) {
    const input = document.getElementById(inputId);
    if (input.type === "password") {
      input.type = "text";
      iconElement.classList.remove("fa-eye-slash");
      iconElement.classList.add("fa-eye");
    } else {
      input.type = "password";
      iconElement.classList.remove("fa-eye");
      iconElement.classList.add("fa-eye-slash");
    }
  }
  function validateForm() {
  const email = document.querySelector('input[name="email"]').value.trim();
  const confirmEmail = document.querySelector('input[name="confirm_email"]').value.trim();
  const password = document.getElementById('newPass').value.trim();
  const confirmPassword = document.getElementById('confirmPass').value.trim();

  if (email !== confirmEmail) {
    alert("Email and Confirm Email do not match.");
    return false;
  }

  if (password !== confirmPassword) {
    alert("Password and Confirm Password do not match.");
    return false;
  }

  return true; // allow form submission
}

</script>
</body>
</html>
''')
