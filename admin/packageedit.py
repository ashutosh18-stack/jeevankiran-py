#!C:/Python312/python.exe
import cgi
import cgitb
import header
import mysql.connector
import os

cgitb.enable()

form = cgi.FieldStorage()
package_id = form.getvalue('package_id')

# Connect to DB
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
mycursor = mydb.cursor(dictionary=True)

# JOIN query to fetch project name
query = f"""
SELECT 
    packagemaster.package_id,
    projectmaster.project_id,
    projectmaster.project_title AS project_name,
    packagemaster.package_item,
    packagemaster.package_qty,
    packagemaster.package_price,
    packagemaster.package_description,
    packagemaster.package_status,
    packagemaster.package_img
FROM packagemaster
JOIN projectmaster ON packagemaster.project_id = projectmaster.project_id
WHERE packagemaster.package_id = {package_id}
"""
mycursor.execute(query)
result = mycursor.fetchone()

project_id = result['project_id']
project_name = result['project_name']
package_item = result['package_item']
package_qty = result['package_qty']
package_price = result['package_price']
package_description = result['package_description']
package_status = result['package_status']
package_img = result['package_img']

folder_name = str(package_id)
img = f"{folder_name}/{package_img}" if package_img else ""

switch_active = "active" if package_status == "Active" else ""
switch_text = "Active" if package_status == "Active" else "Completed"
cursor=mydb.cursor(dictionary=True)
project_query=(f""" SELECT * FROM projectmaster WHERE status='Active'""")
cursor.execute(project_query)
project=cursor.fetchall()

print(f""" 
<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Edit Package</title>
  <link rel="stylesheet" href="style/packagecreate.css"/>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
</head>
<body>

  <div class="wrapper">
    <div class="page-heading">
      <i class="fas fa-box-open"></i> Edit Package Master
    </div>

    <form class="form-container" id="packageForm" action="backend/packageupdatebackend.py" method="post" enctype="multipart/form-data">

      <!-- Image Upload -->
      <label for="packageImage">Package Image Upload</label><br><br>
      <div class="image-upload-wrapper">
        <label class="image-box">
          <input type="file" name="image1" accept="image/*" onchange="previewImage(this)">
          <img src="backend/packageuploads/{img}" class="preview-img" style="display:{'block' if img else 'none'};">
          <span style="display:{'none' if img else 'inline'};">Upload</span>
        </label>
      </div>

      <!-- Active Project Selection -->
      <div class="form-group">
        <label for="project">Select Active Project</label>
        <select name="project" id="project" required>
          <option value="{project_id}">{project_name}</option>
 """)
for proj in project:
    project_id1 = proj['project_id']
    project_name1= proj['project_title']
print(f"""     
            <option value="{project_id1}" >{project_name1}</option>
            """)
print(f"""
        </select>
      </div>

      <!-- Package ID (Read-only) -->
      <div class="form-group">
        <label for="id">Package ID</label>
        <input type="text" id="id" value="{package_id}" name="id" readonly>
      </div>

      <!-- Item Name -->
      <div class="form-group">
        <label for="item">Item Name</label>
        <input type="text" id="item" value="{package_item}" name="item" required>
      </div>

      <!-- Quantity & Price -->
      <div class="qty-price-wrapper">
        <div class="form-group">
          <label for="qty">Quantity</label>
          <input type="number" id="qty" value="{package_qty}" name="qty" min="1" required>
        </div>

        <div class="form-group">
          <label for="price">Price (Rs)</label>
          <input type="number" id="price" value="{package_price}" name="price" min="0" step="0.01" required>
        </div>
      </div>

      <!-- Description -->
      <div class="form-group">
        <label for="description">Description</label>
        <textarea id="description" name="description" required>{package_description}</textarea>
      </div>

      <!-- Status Toggle -->
      <div class="form-group">
        <label>Status</label>
        <div class="switch {switch_active}" id="toggleSwitch">
          <div class="circle"></div>
          <div class="switch-text" id="switchText">{switch_text}</div>
        </div>
        <input type="hidden" name="status" id="statusInput" value="{package_status}">
      </div>

      <!-- Submit Button -->
      <button type="submit" class="submit-btn">Update Package</button>
    </form>
  </div>
""")
print("""
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
""")
