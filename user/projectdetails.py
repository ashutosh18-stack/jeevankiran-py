#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
import mysql.connector
import header
form =cgi.FieldStorage()
project_id=form.getvalue('project_id')

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
cursor = mydb.cursor(dictionary=True)

# Fetch project details
cursor.execute(f"SELECT * FROM projectmaster WHERE project_id = '{project_id}'")
project = cursor.fetchone()

project_title = project['project_title']
id = project['project_id']
image = project['project_img2'];
image2 =project['project_img3'];
image_path= f''' ../admin/backend/projectuploads/{id}/{image}'''
image_path2= f''' ../admin/backend/projectuploads/{id}/{image2}'''
print('''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Hero Slider Scrolling</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    html, body {
      height: 100%;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background-color: #1c1c1c;
      color: white;
      overflow-x: hidden;
    }

    .hero-wrap {
      position: relative;
      width: 100%;
      height: 100vh;
      overflow: hidden;
    }

    .slider {
      display: flex;
      width: 200%;
      height: 100%;
      animation: slideLeft 20s linear infinite;
    }

    .slide {
      flex: 0 0 50%;
      height: 100%;
      background-size: cover;
      background-position: center;
      filter: brightness(1.0);
    }

   

    @keyframes slideLeft {
      0% { transform: translateX(0); }
      100% { transform: translateX(-50%); }
    }

    .overlay-text {
      position: absolute;
      top: 100px; /* 100px from the top of the hero section */
      width: 100%;
 background:  rgba(88, 81, 81, 0.458);    color: white;
      padding: 20px 10px;
      text-align: center;
      font-size: 2rem;
      font-weight: bold;
      z-index: 2;
      border-bottom: 2px solid orange;
      text-transform: uppercase;
    }

    .overlay-text span {
      color: white;
    }

    @media screen and (max-width: 768px) {
      .overlay-text {
        font-size: 1.2rem;
        padding: 15px;
      }
    }

    
  </style>
</head>
<body>
''')

     



print(f'''
  <div class="hero-wrap">
    <div class="slider">
      <div class="slide slide1" style="background-image: url('{image_path}');"></div>
      <div class="slide slide2" style="background-image: url('{image_path2}');"></div>
    </div>
    <div class="overlay-text"><span>{project_title}</span></div>
  </div>

  

</body>
</html>
''')
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

''')

print(f'''
 

<section class="ftco-section">
  <div class="container">
    <div class="row">
      <!-- Shiksha Daan Donation Items -->
      <div class="col-md-3 mb-4">
        <div class="project-card text-center p-3">
          <img src="images/books.jpg" alt="Books" class="project-img mb-3">
          <h5>Books</h5>
          <p>Help children with note books, story books, school books , and more.</p>
          <button class="btn btn-primary">Donate</button>
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
