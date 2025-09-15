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
      
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css" integrity="sha512-5A8nwdMOWrSz20fDsjczgUidUBR8liPYU+WymTZP1lmY9G6Oc7HlZv156XqnsgNUzTyMefFTcsFH/tnJE/+xBg==" crossorigin="anonymous" referrerpolicy="no-referrer" />
  </head>
  <body>
      


      <div class="hero-wrap" style="background-image: url('images/bg_1.jpg');" data-stellar-background-ratio="0.5">
      <div class="overlay"></div>
      <div class="container">
        <div class="row no-gutters slider-text align-items-center justify-content-center" data-scrollax-parent="true">
          <div class="col-md-7 ftco-animate text-center" data-scrollax=" properties: { translateY: '70%' }">
             <p class="breadcrumbs" data-scrollax="properties: { translateY: '30%', opacity: 1.6 }"><span class="mr-2"><a href="index.html"></a></span> <span>Events</span></p>
            <h1 class="mb-3 bread" data-scrollax="properties: { translateY: '30%', opacity: 1.6 }">Compaigns details</h1>
          </div>
        </div>
      </div>
    </div>
      
      

<!--  Welcome to JeevanKiran Jeevan Daan -->
<section class="ftco-section">
  <div class="container">
    <div class="row d-flex">
      <div class="col-md-6 d-flex ftco-animate">
        <div class="img img-about align-self-stretch" style="background-image: url(images/bg_3.jpg); width: 100%;"></div>
      </div>
      <div class="col-md-6 pl-md-5 ftco-animate">
        <h2 class="mb-4">Welcome to JeevanKiran Jeevan Daan</h2>
        <p>
          JeevanKiran Jeevan Daan is a life-saving campaign focused on promoting the culture of voluntary blood donation, organ donation awareness, and emergency medical aid. Every drop, every gesture, and every act of giving has the power to save lives.
        </p>
        <p>
          This initiative is about the most generous gift — the gift of life. Through awareness drives, donor registration, and emergency support, we empower communities to become life-givers.
        </p>
      </div>
    </div>
  </div>
</section>
      
<!--  Jeevan Daan Objectives -->
<section style="background-color: #f8f9fa; padding: 60px 0;">
  <div style="max-width: 850px; margin: 0 auto; text-align: center;">
    <h2 style="font-size: 30px; margin-bottom: 20px;"><i class="fa fa-heartbeat" aria-hidden="true"></i> Our Objectives</h2>
    <p style="font-size: 16px; color: #555; margin-bottom: 30px;">
      Jeevan Daan aims to save lives by building a strong network of voluntary donors and raising awareness about the importance of timely donations.
    </p>
    <ul style="list-style: none; padding: 0; font-size: 18px; text-align: left; margin: 0 auto; max-width: 600px;">
      <li style="margin-bottom: 12px;"><i class="fa fa-arrow-right" aria-hidden="true"></i> Organize regular blood donation camps</li>
      <li style="margin-bottom: 12px;"><i class="fa fa-arrow-right" aria-hidden="true"></i> Promote organ donation awareness and pledge programs</li>
      <li style="margin-bottom: 12px;"><i class="fa fa-arrow-right" aria-hidden="true"></i> Build an emergency donor network database</li>
      <li style="margin-bottom: 12px;"><i class="fa fa-arrow-right" aria-hidden="true"></i> Collaborate with hospitals and NGOs for critical care</li>
      <li style="margin-bottom: 12px;"><i class="fa fa-arrow-right" aria-hidden="true"></i> Educate communities on ethical and legal aspects of donation</li>
    </ul>
  </div>
</section>

<!--  How You Can Support Jeevan Daan -->
<section style="background-color: #fff; padding: 60px 0;">
  <div style="max-width: 850px; margin: 0 auto; text-align: center;">
    <h2 style="font-size: 30px; margin-bottom: 20px;"><i class="fa fa-handshake-o" aria-hidden="true"></i> How You Can Support Jeevan Daan</h2>
    <p style="font-size: 16px; color: #555; margin-bottom: 30px;">
      Your gift can be someone’s second chance at life. Here's how you can support Jeevan Daan:
    </p>
    <ul style="list-style: none; padding: 0; font-size: 18px; text-align: left; margin: 0 auto; max-width: 600px;">
      <li style="margin-bottom: 12px;"><strong>Donate Blood</strong> — just one unit can save up to 3 lives</li>
      <li style="margin-bottom: 12px;">Pledge your organs for donation</li>
      <li style="margin-bottom: 12px;">Volunteer in donor registration and awareness camps</li>
      <li style="margin-bottom: 12px;">Spread the word and encourage others to give the gift of life</li>
    </ul>
  </div>
</section>

<!--  What Your Contribution Does -->
<section style="background-color: #f1f9f6; padding: 60px 0;">
  <div style="max-width: 850px; margin: 0 auto; text-align: center;">
    <h2 style="font-size: 30px; margin-bottom: 20px;"><i class="fa fa-tint" aria-hidden="true"></i> What Your Contribution Does</h2>
    <ul style="list-style: none; padding: 0; font-size: 18px; text-align: left; margin: 0 auto; max-width: 600px;">
      <li style="margin-bottom: 12px;"><strong><i class="fa fa-inr" aria-hidden="true"></i>300:</strong> Supports registration and refreshments for 5 blood donors</li>
      <li style="margin-bottom: 12px;"><strong><i class="fa fa-inr" aria-hidden="true"></i>500:</strong> Funds printing of 100 awareness leaflets or organ donor cards</li>
      <li style="margin-bottom: 12px;"><strong><i class="fa fa-inr" aria-hidden="true"></i>1,000:</strong> Supports a small awareness camp in a local community</li>
      <li style="margin-bottom: 12px;"><strong><i class="fa fa-inr" aria-hidden="true"></i>5,000+:</strong> Enables a full-fledged blood donation or organ awareness drive</li>
    </ul>
  </div>
</section>

<!--  Impact So Far -->
<section style="background-color: #fff; padding: 60px 0;">
  <div style="max-width: 850px; margin: 0 auto; text-align: center;">
    <h2 style="font-size: 30px; margin-bottom: 20px;"><i class="fa fa-bar-chart" aria-hidden="true"></i> Impact So Far</h2>
    <ul style="list-style: none; padding: 0; font-size: 18px; text-align: left; margin: 0 auto; max-width: 600px;">
      <li style="margin-bottom: 12px;"> 1,200+ units of blood collected through camps</li>
      <li style="margin-bottom: 12px;"> 800+ individuals registered as potential organ donors</li>
      <li style="margin-bottom: 12px;"> 50+ awareness events conducted in rural and urban areas</li>
      <li style="margin-bottom: 12px;"> 200+ volunteers trained for life-saving outreach</li>
    </ul>
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