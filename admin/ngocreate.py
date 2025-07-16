#!C:/Python312/python.exe
import cgi
import cgitb
cgitb.enable()
import header

print('''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Add NGO</title>
  <link rel="stylesheet" href="style/ngocreate.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
</head>
<body>

<div class="wrapper">
  <h2><i class="fas fa-building"></i> Add NGO Master</h2>

  <form action="backend/ngocreatebackend.py" method="post" enctype="multipart/form-data" class="ngo-form">

    <!-- Upload Logo Section FIRST -->
    <div class="form-group full-width">
      <label for="logo">Upload Logo</label>
      <div class="image-upload-box" id="uploadBox">
        <input type="file" id="logo" name="logo" accept="image/*" required>
        <span id="uploadText">Upload</span>
        <img id="logoPreview" class="preview-img" src="" alt="Preview">
      </div>
    </div>

    <!-- Rest of the Form -->
    <div class="form-row">
      <div class="form-group">
        <label for="ngo_name">NGO Name</label>
        <input type="text" id="ngo_name" name="ngo_name" required>
      </div>

      <div class="form-group">
        <label for="email">Email Address</label>
        <input type="email" id="email" name="email" required>
      </div>
    </div>

    <div class="form-row">
      <div class="form-group">
        <label for="phone">Phone Number</label>
        <input type="tel" id="phone" name="phone" required>
      </div>

      <div class="form-group">
        <label for="facebook">Facebook Link</label>
        <input type="url" id="facebook" name="facebook">
      </div>
    </div>

    <div class="form-row">
      <div class="form-group">
        <label for="twitter">Twitter Link</label>
        <input type="url" id="twitter" name="twitter">
      </div>

      <div class="form-group">
        <label for="instagram">Instagram Link</label>
        <input type="url" id="instagram" name="instagram">
      </div>
    </div>

    <div class="form-group full-width">
      <label for="description">Description</label>
      <input type="text" id="description" name="description" required>
    </div>

    <div class="form-group full-width">
      <label for="address">Address</label>
      <input type="text" id="address" name="address" required>
    </div>

    <!-- Buttons Section -->
    <div class="form-actions button-group">
      <button type="submit" class="submit-btn">Add NGO</button>
      <a href="./ngomaster.py" class="cancel-btn">Cancel</a>
    </div>

  </form>
</div>

<script>
  const logoInput = document.getElementById('logo');
  const logoPreview = document.getElementById('logoPreview');
  const uploadText = document.getElementById('uploadText');

  logoInput.addEventListener('change', () => {
    const file = logoInput.files[0];
    if (file) {
      logoPreview.src = URL.createObjectURL(file);
      logoPreview.style.display = 'block';
      uploadText.style.display = 'none';
    }
  });
</script>

</body>
</html>
''')
