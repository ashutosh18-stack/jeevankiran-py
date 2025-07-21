#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
import header
import mysql.connector
import os

form = cgi.FieldStorage()
project_id = form.getvalue("project_id")

# DB connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
mycursor = mydb.cursor()
query = f"SELECT * FROM projectmaster WHERE project_id={project_id}"
mycursor.execute(query)
myresult = mycursor.fetchone()

project_title = myresult[1]
project_description = myresult[2]
project_status = myresult[3]

folder_name = str(project_id)
img1 = f"{folder_name}/{myresult[4]}" if myresult[4] else ""
img2 = f"{folder_name}/{myresult[5]}" if myresult[5] else ""
img3 = f"{folder_name}/{myresult[6]}" if myresult[6] else ""

switch_active = "active" if project_status == "Active" else ""
switch_text = "Active" if project_status == "Active" else "Completed"

print(f''' 
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Edit Project</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
  <link rel="stylesheet" href="style/projectedit.css">
</head>
<body>

  <div class="wrapper">
    <div class="page-heading">
      <i class="fas fa-building"></i> Edit Project
    </div>

    <form class="form-container" id="projectForm" action="backend/projectupdatebackend.py" method="post" enctype="multipart/form-data">
    
      <!-- Image Uploads --> 
      <label>Project Images</label><br><br>
      <div class="image-upload-wrapper">
        <label class="image-box">
          <input type="file" name="image1" accept="image/*" onchange="previewImage(this)">
          <img src="backend/projectuploads/{img1}" class="preview-img" style="display:{'block' if img1 else 'none'};">
          <span style="display:{'none' if img1 else 'inline'};">Upload</span>
        </label>
        <label class="image-box">
          <input type="file" name="image2" accept="image/*" onchange="previewImage(this)">
          <img src="backend/projectuploads/{img2}" class="preview-img" style="display:{'block' if img2 else 'none'};">
          <span style="display:{'none' if img2 else 'inline'};">Upload</span>
        </label>
        <label class="image-box">
          <input type="file" name="image3" accept="image/*" onchange="previewImage(this)">
          <img src="backend/projectuploads/{img3}" class="preview-img" style="display:{'block' if img3 else 'none'};">
          <span style="display:{'none' if img3 else 'inline'};">Upload</span>
        </label>
      </div>

      <!-- Project ID (Hidden) -->
      <div class="form-group">
        <label for="title">Project ID</label>
        <input type="text" name="project_id" value="{project_id}" readonly>
      </div>

      <!-- Project Title -->
      <div class="form-group">
        <label for="title">Project Title</label>
        <input type="text" id="title" name="title" value="{project_title}" required>
      </div>

      <!-- Description -->
      <div class="form-group">
        <label for="description">Description</label>
        <input type="text" id="description" name="description" value="{project_description}" required>
      </div>

      <!-- Status Toggle -->
      <div class="form-group">
        <label>Status</label>
        <div class="switch {switch_active}" id="toggleSwitch">
          <div class="circle"></div>
          <div class="switch-text" id="switchText">{switch_text}</div>
        </div>
        <input type="hidden" name="status" id="statusInput" value="{project_status}">
      </div>

      <!-- Submit Button -->
      <button type="submit" class="submit-btn">Update Project</button>
    </form>
  </div>
''')

# JavaScript
print('''
  <script>
    function previewImage(input) {
      const file = input.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
          const previewImg = input.parentElement.querySelector('.preview-img');
          previewImg.src = e.target.result;
          previewImg.style.display = 'block';
          input.parentElement.querySelector('span').style.display = 'none';
        };
        reader.readAsDataURL(file);
      }
    }

    const toggleSwitch = document.getElementById("toggleSwitch");
    const switchText = document.getElementById("switchText");
    const statusInput = document.getElementById("statusInput");

    toggleSwitch.addEventListener("click", () => {
      toggleSwitch.classList.toggle("active");
      const isActive = toggleSwitch.classList.contains("active");
      switchText.textContent = isActive ? "Active" : "Completed";
      statusInput.value = isActive ? "Active" : "Completed";
    });
  </script>

</body>
</html>
''')
