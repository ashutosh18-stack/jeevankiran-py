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
  <title>Green India Project Packages</title>
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
    <h1 class="text-white">Green India Project</h1>
  </div>
</div>

<section class="ftco-section">
  <div class="container">
    <div class="row">
      <!-- Green India Project Items -->
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/tree_planting.jpg" alt="Tree Planting" class="project-img mb-3">
          <h5>Tree Saplings</h5>
          <p>Contribute tree saplings to promote afforestation and greener cities.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/clean_up_drive.jpg" alt="Clean-Up Drives" class="project-img mb-3">
          <h5>Clean-Up Drives</h5>
          <p>Support cleaning materials and logistics for beach, park, and street clean-up initiatives.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/reusable_bags.jpg" alt="Reusable Bags" class="project-img mb-3">
          <h5>Reusable Bags</h5>
          <p>Encourage eco-friendly practices by donating cloth or jute bags.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/solar_lights.jpg" alt="Solar Lights" class="project-img mb-3">
          <h5>Solar Lights</h5>
          <p>Help remote villages reduce carbon footprint with solar-powered lighting.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/garden_tools.jpg" alt="Gardening Tools" class="project-img mb-3">
          <h5>Gardening Tools</h5>
          <p>Donate tools to empower communities for local gardening and farming.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/compost_bins.jpg" alt="Compost Bins" class="project-img mb-3">
          <h5>Compost Bins</h5>
          <p>Help promote zero-waste living by supporting compost bin setups.</p>
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
