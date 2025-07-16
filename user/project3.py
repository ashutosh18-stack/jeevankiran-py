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
      <!-- Food Donation Items -->
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/ration_kit.jpg" alt="Ration Kits" class="project-img mb-3">
          <h5>Ration Kits</h5>
          <p>Donate kits containing rice , wheat , pulses , oil, and spices.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/milk_powder.jpg" alt="Milk Powder" class="project-img mb-3">
          <h5>Milk Powder</h5>
          <p>Provide nutrition for children and infants through milk powder donations.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/snacks.jpg" alt="Healthy Snacks" class="project-img mb-3">
          <h5>Healthy Snacks</h5>
          <p>Contribute nutritious snacks like fruits, dry fruits, or granola bars.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/ready_meals.jpg" alt="Ready-to-Eat Meals" class="project-img mb-3">
          <h5>Ready-to-Eat Meals</h5>
          <p>Support those in need with pre-cooked or easy-to-make meal kits.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/water_bottles.jpg" alt="Drinking Water" class="project-img mb-3">
          <h5>Drinking Water</h5>
          <p>Donate bottled water or install clean water dispensers in rural areas.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/baby_food.jpg" alt="Baby Food" class="project-img mb-3">
          <h5>Baby Food</h5>
          <p>Provide nutritious baby <br>food and cereals for infants in need.</p>
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
