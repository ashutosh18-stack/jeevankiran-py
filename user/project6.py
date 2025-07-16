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
  <title>Homeless Support Packages</title>
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
    <h1 class="text-white">Support for Homeless People</h1>
  </div>
</div>

<section class="ftco-section">
  <div class="container">
    <div class="row">
      <!-- Homeless Support Items -->
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/blankets.jpg" alt="Blankets" class="project-img mb-3">
          <h5>Blankets</h5>
          <p>Donate warm blankets to protect the homeless from cold weather.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/clothes.jpg" alt="Clothes" class="project-img mb-3">
          <h5>Clothing</h5>
          <p>Provide clean and warm clothes including jackets, socks, and gloves.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/food_kit.jpg" alt="Food Kits" class="project-img mb-3">
          <h5>Food Kits</h5>
          <p>Contribute ready-to-eat meals, snacks, and water bottles for daily sustenance.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/shelter_supplies.jpg" alt="Shelter Supplies" class="project-img mb-3">
          <h5>Shelter Supplies</h5>
          <p>Help with sleeping mats, tarpaulins, and tents for temporary protection.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/toiletries.jpg" alt="Toiletries" class="project-img mb-3">
          <h5>Hygiene Kits</h5>
          <p>Provide soap, toothbrushes, sanitary napkins, and other hygiene essentials.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/first_aid.jpg" alt="First Aid Kits" class="project-img mb-3">
          <h5>First Aid Kits</h5>
          <p>Donate basic first aid kits to address minor injuries and health needs.</p>
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
