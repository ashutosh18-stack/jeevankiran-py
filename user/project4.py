#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
import header
print('''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Charity Project Packages</title>
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <link rel="stylesheet" href="css/bootstrap.min.css">
  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <style>
    .project-card {
      border: 1px solid #ddd;
      border-radius: 10px;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
      overflow: hidden;
      transition: 0.3s;
      background-color: #fff;
    }
    .project-card:hover {
      transform: translateY(-5px);
    }
    .project-img {
      width: 100%;
      height: 200px;
      object-fit: cover;
    }
    .status-btn.active {
      background-color: #87CEFA;
      color: white;
    }
    .status-btn.inactive {
      background-color: #dc3545;
      color: white;
    }
  </style>
</head>
<body>

<div class="hero-wrap" style="background-image: url('images/bg_1.jpg'); height: 250px;">
  <div class="overlay"></div>
  <div class="container text-center d-flex justify-content-center align-items-center" style="height: 250px;">
    <h1 class="text-white">Charity Project Packages</h1>
  </div>
</div>

<section class="ftco-section">
  <div class="container">
    <div class="row">
      <!-- Women Needs Donation Items -->
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/sanitary_pads.jpg" alt="Sanitary Pads" class="project-img mb-3">
          <h5>Sanitary Pads</h5>
          <p>Support menstrual hygiene by donating sanitary napkins to women in need.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/personal_hygiene.jpg" alt="Personal Hygiene Kits" class="project-img mb-3">
          <h5>Hygiene Kits</h5>
          <p>Provide soaps, toothpaste, shampoo, and hygiene products for women.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/undergarments.jpg" alt="Undergarments" class="project-img mb-3">
          <h5>Undergarments</h5>
          <p>Donate clean and new undergarments to promote dignity and health.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/women_clothing.jpg" alt="Women Clothing" class="project-img mb-3">
          <h5>Women Clothing</h5>
          <p>Provide sarees, salwar suits, and other clothes for underprivileged women.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/maternity_kit.jpg" alt="Maternity Kits" class="project-img mb-3">
          <h5>Maternity Kits</h5>
          <p>Help pregnant women with maternity essentials and care kits.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/nutrition.jpg" alt="Nutrition Supplements" class="project-img mb-3">
          <h5>Nutrition Supplements</h5>
          <p>Provide protein powders, iron & calcium tablets for women's health.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
    </div>
  </div>
</section>

<script src="js/jquery.min.js"></script>
<script src="js/bootstrap.min.js"></script>
</body>
</html>
''')
import footer
