#!C:/Python312/python.exe
import cgi
import cgitb
cgitb.enable()
import header
import mysql.connector

form = cgi.FieldStorage()
ngo_id = form.getvalue("ngo_id")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
mycursor = mydb.cursor()
query = f"SELECT * FROM ngomaster WHERE ngo_id={ngo_id}"
mycursor.execute(query)
myresult = mycursor.fetchone()

print(f'''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Edit NGO Master</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
  <link rel="stylesheet" href="style/ngomasteredit.css">
</head>
<body>

<div class="wrapper">
  <h2><i class="fas fa-building"></i> Edit NGO Master</h2>

  <form action="backend/ngomasterupdate.py" method="post" enctype="multipart/form-data" class="ngo-form">

    <div class="form-row">
      <div class="form-group">
        <label for="ngo_id">NGO ID</label>
        <input type="text" id="ngo_id" name="ngo_id" value="{myresult[0]}" readonly>
      </div>

      <!-- Image Upload Box Right Side -->
      <div class="form-group">
        <label>Current Logo</label>
        <div class="image-upload-box">
          <input type="file" id="edit_logo" name="edit_logo" accept="image/*">
          <span id="uploadText">Change</span>
          <img src="backend/ngomasteruploads/{myresult[4]}" id="logoPreview" class="preview-img" />
        </div>
      </div>
    </div>

    <div class="form-row">
      <div class="form-group">
        <label for="edit_ngo_name">NGO Name</label>
        <input type="text" id="edit_ngo_name" name="edit_ngo_name" value="{myresult[1]}" required>
      </div>

      <div class="form-group">
        <label for="edit_email">Email Address</label>
        <input type="email" id="edit_email" name="edit_email" value="{myresult[2]}" required>
      </div>
    </div>

    <div class="form-row">
      <div class="form-group">
        <label for="edit_phone">Phone Number</label>
        <input type="tel" id="edit_phone" name="edit_phone" value="{myresult[3]}" required>
      </div>

      <div class="form-group">
        <label for="edit_facebook">Facebook Link</label>
        <input type="url" id="edit_facebook" name="edit_facebook" value="{myresult[9]}">
      </div>
    </div>

    <div class="form-row">
      <div class="form-group">
        <label for="edit_twitter">Twitter Link</label>
        <input type="url" id="edit_twitter" name="edit_twitter" value="{myresult[8]}">
      </div>

      <div class="form-group">
        <label for="edit_instagram">Instagram Link</label>
        <input type="url" id="edit_instagram" name="edit_instagram" value="{myresult[7]}">
      </div>
    </div>

    <div class="form-group full-width">
      <label for="edit_description">Description</label>
      <input type="text" id="edit_description" name="edit_description" value="{myresult[5]}" required>
    </div>

    <div class="form-group full-width">
      <label for="edit_address">Address</label>
      <input type="text" id="edit_address" name="edit_address" value="{myresult[6]}" required>
    </div>

    <div class="form-actions">
      <button type="submit" class="submit-btn">Update NGO</button>
      <a href="ngomasterlist.py" class="cancel-btn">Cancel</a>
    </div>

  </form>
</div>

</body>
</html>
''')
