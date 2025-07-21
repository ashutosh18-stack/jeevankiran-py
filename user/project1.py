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
      <!-- Shiksha Daan Donation Items -->
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/books.jpg" alt="Books" class="project-img mb-3">
          <h5>Books</h5>
          <p>Help children with note books, story books, school books , and more.</p>
          <a href="projectdonor.py"><button class="btn btn-primary">Donate</button></a>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/uniform.jpg" alt="Uniforms" class="project-img mb-3">
          <h5>Uniforms</h5>
          <p>Provide neat and clean uniforms for children to attend school with dignity.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/pens.jpg" alt="Stationery" class="project-img mb-3">
          <h5>Stationery</h5>
          <p>Donate pens, pencils, erasers, and other essentials for learning.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/educational_tools.jpg" alt="Educational Tools" class="project-img mb-3">
          <h5>Educational Tools</h5>
          <p>Help with learning aids like charts, models, and drawing kits.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>

      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/shoes.jpg" alt="Shoes and Socks" class="project-img mb-3">
          <h5>Shoes and Socks</h5>
          <p>Donate school shoes and socks to keep feet warm and protected.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/schoolbag.jpg" alt="School Bags" class="project-img mb-3">
          <h5>School Bags</h5>
          <p>Provide strong and durable bags to carry school essentials.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/games.jpg" alt="Learning Games" class="project-img mb-3">
          <h5>Learning Games</h5>
          <p>Donate educational games that help children learn through play.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/headphones.jpg" alt="Headphones" class="project-img mb-3">
          <h5>Headphones</h5>
          <p>Support students attending online classes with good quality headphones.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/exam_fees.jpg" alt="Exam Fees" class="project-img mb-3">
          <h5>Exam Fees</h5>
          <p>Help cover exam fees for students from financially weak backgrounds.</p>
          <button class="btn btn-primary">Donate</button>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/tablet.jpg" alt="Tablets" class="project-img mb-3">
          <h5>Tablets</h5>
          <p>Donate used or new tablets to enable digital education for children.</p>
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
