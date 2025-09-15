#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
import header
import cgi
import cgitb
cgitb.enable()
import mysql.connector


form = cgi.FieldStorage()
package_id = form.getvalue('package_id')
user_id = form.getvalue("id")
# Fetch package details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
cursor = mydb.cursor(dictionary=True)
cursor.execute("SELECT * FROM packagemaster WHERE package_id = %s", (package_id,))
package = cursor.fetchone()

item = package['package_item']
project_id = package['project_id'] 
total_price = int(package['package_price'])
required_qty = int(package['package_qty'])
unit_price = total_price // required_qty  

cursor.execute("SELECT project_title FROM projectmaster WHERE project_id = %s", (project_id,))
project_data = cursor.fetchone()
project_name = project_data['project_title']

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


<section class="ftco-section-3 img" style="background-image: url(images/bg_3.jpg);">
  <div class="overlay"></div>
  <div class="container">
    <div class="row d-md-flex">
      <div class="col-md-6 d-flex ftco-animate">
        <div class="img img-2 align-self-stretch" style="background-image: url(images/bg_4.jpg);"></div>
      </div>
      <div class="col-md-6 volunteer pl-md-5 ftco-animate">
        <h3 class="mb-3">Make a Donation</h3>
      ''')
print(f'''
<form action="backend/projectdonorbackend.py" method="post" class="donation-form" >
        <input type="hidden" name="userid" value="{user_id}">
  <input type="hidden" name="package_id" value="{package_id}">
  <div class="form-group">
    <input type="text" class="form-control" name="name" placeholder="Your Name" required>
  </div>
  <div class="form-group">
    <input type="email" class="form-control" name="email" placeholder="Your Email" required>
  </div>
  <div class="form-group">
    <input type="text" class="form-control" name="project" value="{project_name}" readonly>
  </div>
  <div class="form-group">
    <input type="text" class="form-control" name="item" value="{item}" readonly>
  </div>
  <div class="form-group">
    <input type="number" class="form-control" id="quantity" name="quantity" min="1" placeholder="Max {required_qty} available" oninput="calculateAmount()" required>
  </div>
  <div class="form-group">
    <input type="number" class="form-control" id="amount" name="amount" value="{unit_price}" readonly>
  </div>
  <div class="form-group">
    <input type="text" class="form-control" name="message" placeholder="Message (Optional)">
  </div>
  <div class="form-group">
    <input type="submit" value="Donate Now" class="btn btn-white py-3 px-5">
  </div>
</form>
''')

print(f'''
      </div>
    </div>
  </div>
</section>

      
      

 <!-- loader -->
  <div id="ftco-loader" class="show fullscreen"><svg class="circular" width="48px" height="48px"><circle class="path-bg" cx="24" cy="24" r="22" fill="none" stroke-width="4" stroke="#eeeeee"/><circle class="path" cx="24" cy="24" r="22" fill="none" stroke-width="4" stroke-miterlimit="10" stroke="#F96D00"/></svg></div>
<script>
  const unitPrice = {unit_price};
  const maxQty = {required_qty};
      ''')
print('''
 function calculateAmount() {
    const qty = parseInt(document.getElementById("quantity").value) || 0;
    if (qty < 1 || qty > maxQty) {
      document.getElementById("amount").value = 0;
    } else {
      document.getElementById("amount").value = qty * unitPrice;
    }
  }

  function validateForm() {
    const qty = parseInt(document.getElementById("quantity").value);
    if (!qty || qty < 1 || qty > maxQty) {
      alert("Please enter a valid quantity between 1 and " + maxQty);
      return false;
    }
    return true;
  }
</script>


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