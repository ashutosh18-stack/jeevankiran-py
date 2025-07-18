#!C:/Python312/python.exe
import cgi
import cgitb
import header
import mysql.connector
import os

cgitb.enable()

# Connect DB
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
mycursor = mydb.cursor(dictionary=True)

query = "SELECT * FROM projectmaster"
mycursor.execute(query)
results = mycursor.fetchall()
print('''
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Welfare - Free Bootstrap 4 Template by Colorlib</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    
    <link href="https://fonts.googleapis.com/css?family=Dosis:200,300,400,500,700" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Overpass:300,400,400i,600,700" rel="stylesheet">

    <link rel="stylesheet" href="css/open-iconic-bootstrap.min.css">
    <link rel="stylesheet" href="css/animate.css">
    
    <link rel="stylesheet" href="css/owl.carousel.min.css">
    <link rel="stylesheet" href="css/owl.theme.default.min.css">
    <link rel="stylesheet" href="css/magnific-popup.css">

    <link rel="stylesheet" href="css/aos.css">

    <link rel="stylesheet" href="css/ionicons.min.css">

    <link rel="stylesheet" href="css/bootstrap-datepicker.css">
    <link rel="stylesheet" href="css/jquery.timepicker.css">

    
    <link rel="stylesheet" href="css/flaticon.css">
    <link rel="stylesheet" href="css/icomoon.css">
    <link rel="stylesheet" href="css/style.css">
      
     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css" integrity="sha512-5A8nwdMOWrSz20fDsjczgUidUBR8liPYU+WymTZP1lmY9G6Oc7HlZv156XqnsgNUzTyMefFTcsFH/tnJE/+xBg==" crossorigin="anonymous" referrerpolicy="no-referrer" />

    <style>
      .status-btn.active {
      background-color: #87CEFA;
      color: white;
    }
    .status-btn.inactive {
      background-color: #dc3545;
      color: white;

      </style>

  </head>
  <body>
    
    <div class="hero-wrap" style="background-image: url('images/bg_5.jpg');" data-stellar-background-ratio="0.5">
      <div class="overlay"></div>
      <div class="container">
        <div class="row no-gutters slider-text align-items-center justify-content-center" data-scrollax-parent="true">
          <div class="col-md-7 ftco-animate text-center" data-scrollax=" properties: { translateY: '70%' }">
             <p class="breadcrumbs" data-scrollax="properties: { translateY: '30%', opacity: 1.6 }"><span class="mr-2"><a href="index.html">Home</a></span> <span>Projects</span></p>
            <h1 class="mb-3 bread" data-scrollax="properties: { translateY: '30%', opacity: 1.6 }">Projects</h1>
          </div>
        </div>
      </div>
    </div>

    
    <section class="ftco-section">
      <div class="container">
      	<div class="row">
''')
for x in results:
    project_title = x['project_title']
    desc = x['project_description']
    status = x['status']
    img1 = x['project_img1']
print(f'''
      		<div class="col-md-4 ftco-animate">
      			<div class="cause-entry">
    					<a href="#" class="img" style="background-image: url(images/cause-1.jpg);"></a>
    					<div class="text p-3 p-md-4">
      
    						<h3><a href="project1.py">{project_title}</a></h3>
    						<p>{desc}</p>
    						<span class="donation-time mb-3 d-block">Last donation 1w ago</span>
                <p><a href="project1.py">Donate <i class="ion-ios-arrow-forward"></i></a></p>
                <div class="progress custom-progress-success">
                  <div class="progress-bar bg-primary" role="progressbar" style="width: 28%" aria-valuenow="28" aria-valuemin="0" aria-valuemax="100"></div>
                </div>
                <span class="fund-raised d-block"><i class="fa fa-inr" aria-hidden="true"></i>12,000 raised of <i class="fa fa-inr" aria-hidden="true"></i>30,000</span>
                <button class="btn status-btn active">{status}</button>
    					</div>
    				</div>
      		</div>
''')
print('''
      		<div class="col-md-4 ftco-animate">
      			<div class="cause-entry">
    					<a href="#" class="img" style="background-image: url(images/cause-2.jpg);"></a>
    					<div class="text p-3 p-md-4">
    						<h3><a href="project2.py">Jeevan Daan (Health & Medical Aid)</a></h3>
    						<p>Purpose: Support free medical checkups, surgeries, and health camps.</p>
    						<span class="donation-time mb-3 d-block">Last donation 1w ago</span>
                <p><a href="project2.py">Donate <i class="ion-ios-arrow-forward"></i></a></p>
                <div class="progress custom-progress-success">
                  <div class="progress-bar bg-primary" role="progressbar" style="width: 28%" aria-valuenow="28" aria-valuemin="0" aria-valuemax="100"></div>
                </div>
                <span class="fund-raised d-block"><i class="fa fa-inr" aria-hidden="true"></i>12,000 raised of <i class="fa fa-inr" aria-hidden="true"></i>30,000</span>
    					  <button class="btn status-btn active">Active</button>
              </div>
    				</div>
      		</div>
      		<div class="col-md-4 ftco-animate">
      			<div class="cause-entry">
    					<a href="#" class="img" style="background-image: url(images/cause-3.jpg);"></a>
    					<div class="text p-3 p-md-4">
    						<h3><a href="project3.py">Bhojan Seva (Food Distribution Program)</a></h3>
    						<p>Purpose: Distribute nutritious meals to homeless families, children, and the elderly.</p>
    						<span class="donation-time mb-3 d-block">Last donation 1w ago</span>
                <p><a href="project3.py">Donate <i class="ion-ios-arrow-forward"></i></a></p>
                <div class="progress custom-progress-success">
                  <div class="progress-bar bg-primary" role="progressbar" style="width: 28%" aria-valuenow="28" aria-valuemin="0" aria-valuemax="100"></div>
                </div>
                <span class="fund-raised d-block"><i class="fa fa-inr" aria-hidden="true"></i>12,000 raised of <i class="fa fa-inr" aria-hidden="true"></i>30,000</span>
    					  <button class="btn status-btn inactive">Non-Active</button>
              </div>
    				</div>
      		</div>
      		<div class="col-md-4 ftco-animate">
      			<div class="cause-entry">
    					<a href="#" class="img" style="background-image: url(images/cause-4.jpg);"></a>
    					<div class="text p-3 p-md-4">
    						<h3><a href="project4.py">Nari Shakti (Women Empowerment)</a></h3>
    						<p>Purpose: Provide skill training, self-help tools, and hygiene kits for women.</p>
    						<span class="donation-time mb-3 d-block">Last donation 1w ago</span>
                <p><a href="project4.py">Donate <i class="ion-ios-arrow-forward"></i></a></p>
                <div class="progress custom-progress-success">
                  <div class="progress-bar bg-primary" role="progressbar" style="width: 28%" aria-valuenow="28" aria-valuemin="0" aria-valuemax="100"></div>
                </div>
                <span class="fund-raised d-block"><i class="fa fa-inr" aria-hidden="true"></i>12,000 raised of <i class="fa fa-inr" aria-hidden="true"></i>30,000</span>
    					  <button class="btn status-btn active">Active</button>
              </div>
    				</div>
      		</div>
      		<div class="col-md-4 ftco-animate">
      			<div class="cause-entry">
    					<a href="#" class="img" style="background-image: url(images/cause-5.jpg);"></a>
    					<div class="text p-3 p-md-4">
    						<h3><a href="project5.py">Harit Bharat (Green India Campaign)</a></h3>
    						<p>Purpose: Organize tree plantations, clean-up drives, and eco-awareness programs.</p>
    						<span class="donation-time mb-3 d-block">Last donation 1w ago</span>
                <p><a href="project5.py">Donate <i class="ion-ios-arrow-forward"></i></a></p>
                <div class="progress custom-progress-success">
                  <div class="progress-bar bg-primary" role="progressbar" style="width: 28%" aria-valuenow="28" aria-valuemin="0" aria-valuemax="100"></div>
                </div>
                <span class="fund-raised d-block"><i class="fa fa-inr" aria-hidden="true"></i>12,000 raised of <i class="fa fa-inr" aria-hidden="true"></i>30,000</span>
    					  <button class="btn status-btn active">Active</button>
              </div>
    				</div>
      		</div>
      		<div class="col-md-4 ftco-animate">
      			<div class="cause-entry">
    					<a href="#" class="img" style="background-image: url(images/cause-6.jpg);"></a>
    					<div class="text p-3 p-md-4">
    						<h3><a href="project6.py">Ashray (Shelter for the Homeless)</a></h3>
    						<p>Purpose: Build or maintain shelters for the homeless and abandoned elderly.</p>
    						<span class="donation-time mb-3 d-block">Last donation 1w ago</span>
                <p><a href="project6.py">Donate <i class="ion-ios-arrow-forward"></i></a></p>
                <div class="progress custom-progress-success">
                  <div class="progress-bar bg-primary" role="progressbar" style="width: 28%" aria-valuenow="28" aria-valuemin="0" aria-valuemax="100"></div>
                </div>
                <span class="fund-raised d-block"><i class="fa fa-inr" aria-hidden="true"></i>12,000 raised of <i class="fa fa-inr" aria-hidden="true"></i>30,000</span>
    					  <button class="btn status-btn active">Active</button>
              </div>
    				</div>
      		</div>
        </div>
        <div class="row mt-5">
          <div class="col text-center">
            <div class="block-27">
              <ul>
                <li><a href="#">&lt;</a></li>
                <li class="active"><span>1</span></li>
                <li><a href="#">2</a></li>
                <li><a href="#">3</a></li>
                <li><a href="#">4</a></li>
                <li><a href="#">5</a></li>
                <li><a href="#">&gt;</a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    
  

  <!-- loader -->
  <div id="ftco-loader" class="show fullscreen"><svg class="circular" width="48px" height="48px"><circle class="path-bg" cx="24" cy="24" r="22" fill="none" stroke-width="4" stroke="#eeeeee"/><circle class="path" cx="24" cy="24" r="22" fill="none" stroke-width="4" stroke-miterlimit="10" stroke="#F96D00"/></svg></div>


  <script src="js/jquery.min.js"></script>
  <script src="js/jquery-migrate-3.0.1.min.js"></script>
  <script src="js/popper.min.js"></script>
  <script src="js/bootstrap.min.js"></script>
  <script src="js/jquery.easing.1.3.js"></script>
  <script src="js/jquery.waypoints.min.js"></script>
  <script src="js/jquery.stellar.min.js"></script>
  <script src="js/owl.carousel.min.js"></script>
  <script src="js/jquery.magnific-popup.min.js"></script>
  <script src="js/aos.js"></script>
  <script src="js/jquery.animateNumber.min.js"></script>
  <script src="js/bootstrap-datepicker.js"></script>
  <script src="js/jquery.timepicker.min.js"></script>
  <script src="js/scrollax.min.js"></script>
  <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBVWaKrjvy3MaE7SQ74_uJiULgl1JY0H2s&sensor=false"></script>
  <script src="js/google-map.js"></script>
  <script src="js/main.js"></script>
    
  </body>
</html>
''')
import footer