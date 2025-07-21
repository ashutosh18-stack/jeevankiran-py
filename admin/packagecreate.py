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
query=(f"SELECT * From projectmaster WHERE status='Active'");
mycursor.execute(query)
result=mycursor.fetchall()
print(''' 
<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Add Package Master</title>
  <link rel="stylesheet" href="style/packagecreate.css"/>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
  <style>
 
  </style>
</head>
<body>

  <div class="wrapper">
    <div class="page-heading">
      <i class="fas fa-box-open"></i> Add Package Master
    </div>

    <form class="form-container" id="packageForm" action="backend/packagecreatebackend.py" method="post" enctype="multipart/form-data">

      <!-- Image Upload -->
      <label for="packageImage">Package Image Upload</label><br><br>
      <div class="image-upload-wrapper">
        <label class="image-box">
          <input type="file" name="packageImage" accept="image/*" onchange="previewImage(this)" required>
          <img src="" class="preview-img">
          <span>Upload</span>
        </label>
      </div>

      <!-- Active Project Selection -->
      <div class="form-group">
        <label for="project">Select Active Project</label>

        <select name="project" id="project" required>
          <option value="">-- Select Project --</option>
''')
for x in result:
    pro_name = x['project_title']
    print(f'''
          <option value="{pro_name}">{pro_name}</option>
   ''')
print('''       
        </select>
      </div>

      <!-- Item Name -->
      <div class="form-group">
        <label for="item">Item Name</label>
        <input type="text" id="item" name="item" placeholder="Enter item name" required>
      </div>

      <div class="qty-price-wrapper">
        <div class="form-group">
          <label for="qty">Quantity</label>
          <input type="number" id="qty" name="qty" min="1" placeholder="Enter quantity" required>
        </div>

        <div class="form-group">
          <label for="price">Price (Rs)</label>
          <input type="number" id="price" name="price" min="0" step="0.01" placeholder="Enter price" required>
        </div>
      </div>

      <!-- Description -->
      <div class="form-group">
        <label for="description">Description</label>
        <textarea id="description" name="description" placeholder="Enter package description" required></textarea>
      </div>
     <div class="form-group">
        <label>Status</label>
        <div class="switch" id="toggleSwitch">
          <div class="circle"></div>
          <div class="switch-text" id="switchText">Completed</div>
        </div>
        <input type="hidden" name="status" id="statusInput" value="Completed">
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
