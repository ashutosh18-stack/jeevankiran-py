#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
import header

print(f'''
  <head>
    <link rel="stylesheet" href="style/ngocreate.css">
  </head>

  <h2 style="margin-bottom: 25px;"><i class="fas fa-building"></i> Add NGO Master</h2>

  <form action="backend/ngocreatebackend.py" method="post" enctype="multipart/form-data" class="ngo-form">
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
        <input type="tel" id="phone" name="phone"  required>
      </div>

      <div class="form-group">
        <label for="logo">Upload Logo</label>
        <input type="file" id="logo" name="logo" accept="image/*" required>
      </div>
    </div>

    <div class="form-group full-width">
      <label for="description">Description</label>
      <input type="text" id="description" name="description" rows="3" required>
    </div>

    <div class="form-group full-width">
      <label for="address">Address</label>
      <input type="text" id="address" name="address" rows="3" required>
    </div>

    <div class="form-row">
      <div class="form-group">
        <label for="facebook">Facebook Link</label>
        <input type="url" id="facebook" name="facebook">
      </div>

      <div class="form-group">
        <label for="twitter">Twitter Link</label>
        <input type="url" id="twitter" name="twitter">
      </div>
    </div>

    <div class="form-group full-width">
      <label for="instagram">Instagram Link</label>
      <input type="url" id="instagram" name="instagram">
    </div>

    <div class="form-actions">
      <button type="submit" class="submit-btn">Add NGO</button>
    </div>
  </form>

</div>
</div>
</body>
</html>
''')
