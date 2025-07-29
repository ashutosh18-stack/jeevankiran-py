#!C:/Python312/python.exe
import cgi
import cgitb
cgitb.enable()
import header

print(''' 
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Add New Campaign Form</title>
  <link rel="stylesheet" href="style/projectcreate.css"/>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
</head>
<body>

  <div class="wrapper">
    <div class="page-heading">
      <i class="fas fa-building"></i> Add Campaign Master
    </div>

    <form class="form-container" id="campaignForm" action="backend/campaigncreatebackend.py" method="post" enctype="multipart/form-data">

      <!-- Image Upload Instructions -->
      <div class="instructions" style="margin-bottom: 15px; background-color: #f0f0f0; padding: 10px; border-left: 4px solid orange;">
        <strong>Image Upload Guidelines:</strong>
        <ul style="margin-top: 5px; padding-left: 20px;">
          <li><strong>Image 1:</strong> Square, <em>500x500</em> pixels, clear and high-quality, <strong>PNG/JPG</strong> format.</li>
          <li><strong>Image 2:</strong> Landscape, <em>1200x800</em> pixels, clear and high-quality, <strong>JPG/PNG</strong> format.</li>
          <li><strong>Image 3:</strong> Landscape, <em>1200x800</em> pixels, clear and high-quality, <strong>JPG/PNG</strong> format.</li>
        </ul>
      </div>

      <!-- Image Uploads --> 
      <label for="title">campaign Images Upload</label><br><br>
      <div class="image-upload-wrapper">
        <label class="image-box">
          <input type="file" name="image1" accept="image/*" onchange="previewImage(this)">
          <img src="" class="preview-img">
          <span>Upload</span>
        </label>
          <label class="image-box">
          <input type="file" name="image2" accept="image/*" onchange="previewImage(this)">
          <img src="" class="preview-img">
          <span>Upload</span>
        </label>
          <label class="image-box">
          <input type="file" name="image3" accept="image/*" onchange="previewImage(this)">
          <img src="" class="preview-img">
          <span>Upload</span>
        </label>
      </div>

      <!-- Campaign Title -->
      <div class="form-group">
        <label for="title">Campaign Title</label>
        <input type="text" id="title" name="title" placeholder="Enter Campaign title" required>
      </div>

      <!-- Description -->
      <div class="form-group">
        <label for="description">Description</label>
        <textarea id="description" name="description" placeholder="Enter Campaign Purpose" required></textarea>
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
      <button type="submit" class="submit-btn">Add Campaign</button>
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

    // Toggle Switch for Status
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
