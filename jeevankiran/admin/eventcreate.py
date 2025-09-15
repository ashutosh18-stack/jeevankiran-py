#!C:/Python312/python.exe
import cgi
import cgitb
cgitb.enable()
import header
import mysql.connector

mydb=mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "jeevankiran"
)
mycursor =mydb.cursor(dictionary=True)
query=(f"SELECT * From campaignmaster WHERE status='Active'");
mycursor.execute(query)
result=mycursor.fetchall()
print(''' 
<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Add Event Master</title>
  <link rel="stylesheet" href="style/packagecreate.css"/>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
  <style>
 
  </style>
</head>
<body>

  <div class="wrapper">
    <div class="page-heading">
      <i class="fas fa-box-open"></i> Add Event Master
    </div>

    <form class="form-container" id="eventForm" action="backend/eventcreatebackend.py" method="post" enctype="multipart/form-data">

      <!-- Image Upload -->
      <label for="eventImage">Event Image Upload</label><br><br>
      <div class="image-upload-wrapper">
        <label class="image-box">
          <input type="file" name="eventImage" accept="image/*" onchange="previewImage(this)" required>
          <img src="" class="preview-img">
          <span>Upload</span>
        </label>
      </div>

      <!-- Active Campaign Selection -->
      <div class="form-group">
        <label for="campaign">Select Active Campaign</label>

        <select name="campaign" id="campaign" required>
          <option value="">-- Select campaign --</option>
''')
for x in result:
    cam_name = x['title']
    print(f'''
          <option value="{cam_name}">{cam_name}</option>
   ''')
print('''       
        </select>
      </div>

      <div class="form-group">
  <label for="description">Description</label>
  <textarea id="description" name="description" class="form-control big-textarea" placeholder="Enter Description" required></textarea>
</div>

<div class="form-group">
  <label for="objectives">Our Objectives</label>
  <textarea id="objectives" name="objectives" class="form-control big-textarea" placeholder="Enter objectives (one per line)" required></textarea>
</div>

<div class="form-group">
  <label for="yourhelp">How You Can Help</label>
  <textarea id="yourhelp" name="yourhelp" class="form-control big-textarea" placeholder="Enter points (one per line)" required></textarea>
</div>

<div class="form-group">
  <label for="contribution">What Your Contribution Does</label>
  <textarea id="contribution" name="contribution" class="form-control big-textarea" placeholder="Enter points (one per line)" required></textarea>
</div>

<div class="form-group">
  <label for="impact">Impact So Far</label>
  <textarea id="impact" name="impact" class="form-control big-textarea" placeholder="Enter points (one per line)" required></textarea>
</div>


      
     <!-- Submit Button -->
      <button type="submit" class="submit-btn">Add Package</button>
    </form>
  </div>

      
      <script>
    function previewImage(input) {
      const file = input.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
          const previewImg = input.parentElement.querySelector('.preview-img');
          const uploadText = input.parentElement.querySelector('span');
          previewImg.src = e.target.result;
          previewImg.style.display = 'block';
          uploadText.style.display = 'none';
        };
        reader.readAsDataURL(file);
      }
    }
      </script>

</body>
</html>
''')
