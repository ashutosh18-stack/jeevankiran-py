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
      <!-- Health & Medical Donation Items -->
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/medicines.jpg" alt="Medicines" class="project-img mb-3">
          <h5>Medicines</h5>
          <p>Provide essential medicines for those who can't afford them.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/first_aid.jpg" alt="First Aid Kits" class="project-img mb-3">
          <h5>First Aid Kits</h5>
          <p>Help provide basic <br>medical kits for emergencies and care.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/health_check.jpg" alt="Health Checkups" class="project-img mb-3">
          <h5>Health Checkups</h5>
          <p>Support basic health checkups for underprivileged communities.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/sanitary.jpg" alt="Sanitary Kits" class="project-img mb-3">
          <h5>Sanitary Kits</h5>
          <p>Provide hygiene kits including soap, sanitizer, and sanitary pads.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/thermometer.jpg" alt="Thermometers" class="project-img mb-3">
          <h5>Thermometers</h5>
          <p>Donate thermometers for homes and clinics in need.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/masks.jpg" alt="Masks and Gloves" class="project-img mb-3">
          <h5>Masks & Gloves</h5>
          <p>Support safety by donating protective masks and gloves.</p>
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
