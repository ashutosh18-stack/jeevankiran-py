#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
import header
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
  </head>
  <body>
    
    
    <div class="hero-wrap" style="background-image: url('images/bg_6.jpg');" data-stellar-background-ratio="0.5">
      <div class="overlay"></div>
      <div class="container">
        <div class="row no-gutters slider-text align-items-center justify-content-center" data-scrollax-parent="true">
          <div class="col-md-7 ftco-animate text-center" data-scrollax=" properties: { translateY: '70%' }">
             <p class="breadcrumbs" data-scrollax="properties: { translateY: '30%', opacity: 1.6 }"><span class="mr-2"><a href="index.html">Home</a></span> <span>Donate</span></p>
            <h1 class="mb-3 bread" data-scrollax="properties: { translateY: '30%', opacity: 1.6 }">Donations</h1>
          </div>
        </div>
      </div>
    </div>

    
<section class="ftco-section bg-light">
  <div class="container">
    <div class="row">

      <!-- 1 -->
      <div class="col-lg-4 d-flex mb-sm-4 ftco-animate">
        <div class="staff">
          <div class="d-flex mb-4">
            <div class="img" style="background-image: url(images/person_1.jpg);"></div>
            <div class="info ml-4">
              <h3><a href="#">Rajesh Kumar</a></h3>
              <span class="position">Donated Just now</span>
              <div class="text">
                <p>Donated <span><i class="fa fa-inr" aria-hidden="true"></i>25,000</span> for <a href="#">Children's Food Aid</a></p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 2 -->
      <div class="col-lg-4 d-flex mb-sm-4 ftco-animate">
        <div class="staff">
          <div class="d-flex mb-4">
            <div class="img" style="background-image: url(images/person_2.jpg);"></div>
            <div class="info ml-4">
              <h3><a href="#">Meera Joshi</a></h3>
              <span class="position">Donated Just now</span>
              <div class="text">
                <p>Donated <span><i class="fa fa-inr" aria-hidden="true"></i>12,000</span> for <a href="#">Medical Support Fund</a></p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 3 -->
      <div class="col-lg-4 d-flex mb-sm-4 ftco-animate">
        <div class="staff">
          <div class="d-flex mb-4">
            <div class="img" style="background-image: url(images/person_3.jpg);"></div>
            <div class="info ml-4">
              <h3><a href="#">Arjun Verma</a></h3>
              <span class="position">Donated Just now</span>
              <div class="text">
                <p>Donated <span><i class="fa fa-inr" aria-hidden="true"></i>20,000</span> for <a href="#">Food & Shelter Drive</a></p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 4 -->
      <div class="col-lg-4 d-flex mb-sm-4 ftco-animate">
        <div class="staff">
          <div class="d-flex mb-4">
            <div class="img" style="background-image: url(images/person_4.jpg);"></div>
            <div class="info ml-4">
              <h3><a href="#">Priya Desai</a></h3>
              <span class="position">Donated Just now</span>
              <div class="text">
                <p>Donated <span><i class="fa fa-inr" aria-hidden="true"></i>25,000</span> for <a href="#">Children's Education</a></p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 5 -->
      <div class="col-lg-4 d-flex mb-sm-4 ftco-animate">
        <div class="staff">
          <div class="d-flex mb-4">
            <div class="img" style="background-image: url(images/person_5.jpg);"></div>
            <div class="info ml-4">
              <h3><a href="#">Vikram Shah</a></h3>
              <span class="position">Donated Just now</span>
              <div class="text">
                <p>Donated <span><i class="fa fa-inr" aria-hidden="true"></i>12,000</span> for <a href="#">Women Empowerment</a></p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 6 -->
      <div class="col-lg-4 d-flex mb-sm-4 ftco-animate">
        <div class="staff">
          <div class="d-flex mb-4">
            <div class="img" style="background-image: url(images/person_6.jpg);"></div>
            <div class="info ml-4">
              <h3><a href="#">Anita Sharma</a></h3>
              <span class="position">Donated Just now</span>
              <div class="text">
                <p>Donated <span><i class="fa fa-inr" aria-hidden="true"></i>20,000</span> for <a href="#">Senior Citizen Support</a></p>
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>

    <!-- Optional Pagination -->
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

      
  <section class="ftco-section-3 img" style="background-image: url(images/bg_3.jpg);">
  <div class="overlay"></div>
  <div class="container">
    <div class="row d-md-flex">
      <div class="col-md-6 d-flex ftco-animate">
        <div class="img img-2 align-self-stretch" style="background-image: url(images/bg_4.jpg);"></div>
      </div>
      <div class="col-md-6 volunteer pl-md-5 ftco-animate">
        <h3 class="mb-3">Make a Donation</h3>
        <form action="backend/donateamtbackend.py" class="donation-form">
          <div class="form-group">
            <input type="text" class="form-control" id="name" name="name" placeholder="Your Name" required>
          </div>
          <div class="form-group">
            <input type="email" class="form-control" id="email" name="email" placeholder="Your Email" required>
          </div>
          <div class="form-group">
            <input type="int" class="form-control" id="amount" name="amount" placeholder="Amount (in rupees)" min="1" required>
          </div>
          <div class="form-group">
            <input type="text" class="form-control" cols="30" rows="3" id="message" name="message"  placeholder="Message (Optional)">
          </div>
          <div class="form-group">
            <input type="submit" value="Donate Now" class="btn btn-white py-3 px-5">
          </div>
        </form>
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