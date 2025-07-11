#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
import header
import mysql.connector
form=cgi.FieldStorage()
ngo_id = form.getvalue("ngo_id")
# print(ngo_id)
mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "",
    database = "jeevankiran"
)
mycursor = mydb.cursor()
query = f"SELECT * FROM ngomaster WHERE ngo_id={ngo_id}"
# print(query)
mycursor.execute(query)
myresult = mycursor.fetchone()
mydb.commit()

print(f'''
  <head>
    <link rel="stylesheet" href="style/ngomasteredit.css">
  </head>

  <h2 style="margin-bottom: 25px;"><i class="fas fa-building"></i> Edit NGO Master</h2>

  <form action="backend/ngomasterupdate.py" method="post" enctype="multipart/form-data" class="ngo-form">
    <div class="form-row">
        <div class="form-group">
        <label for="ngo_id">NGO id</label>
        <input type="text" id="ngo_id" value="{myresult[0]}" name="ngo_id" readonly>
      </div>
      <div class="form-group">
        <label for="ngo_name">NGO Name</label>
        <input type="text" id="edit_ngo_name" value="{myresult[1]}" name="edit_ngo_name" required>
      </div>

      <div class="form-group">
        <label for="email">Email Address</label>
        <input type="email" id="edit_email" value="{myresult[2]}" name="edit_email" required>
      </div>
    </div>

    <div class="form-row">
      <div class="form-group">
        <label for="phone">Phone Number</label>
        <input type="tel" id="edit_phone" value="{myresult[3]}" name="edit_phone"  required>
      </div>

    
    <div class="form-group logo-preview-group">
  <label for="logo">Current Logo</label>
  <div class="logo-preview">
    <img src="backend/ngomasteruploads/{myresult[4]}" alt="Logo" width="70" height="70">
  </div>
  <label for="logo">Change Logo (Optional)</label>
  <input type="file" id="edit_logo" name="edit_logo" accept="image/*">
</div>
    </div>

    <div class="form-group full-width">
      <label for="description">Description</label>
      <input type="text" id="edit_description" value="{myresult[5]}" name="edit_description" rows="3" required>
    </div>

    <div class="form-group full-width">
      <label for="address">Address</label>
      <input type="text" id="edit_address" value="{myresult[6]}" name="edit_address" rows="3" required>
    </div>

    <div class="form-row">
      <div class="form-group">
        <label for="facebook">Facebook Link</label>
        <input type="url" id="edit_facebook" value="{myresult[9]}" name="edit_facebook">
      </div>

      <div class="form-group">
        <label for="twitter">Twitter Link</label>
        <input type="url" id="edit_twitter" value="{myresult[8]}" name="edit_twitter">
      </div>
    </div>

    <div class="form-group full-width">
      <label for="instagram">Instagram Link</label>
      <input type="url" id="edit_instagram" value="{myresult[7]}" name="edit_instagram">
    </div>

  <div class="form-actions">
  <button type="submit" class="submit-btn">Add NGO</button>
  <a href="ngomasterlist.py" class="submit-btn" style="  text-decoration: none;">Cancel</a>
</div>

  </form>

</div>
</div>
</body>
</html>
''')
