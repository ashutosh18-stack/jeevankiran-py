#!C:/Python312/python.exe
import cgi
import mysql.connector
import cgitb
import header  
cgitb.enable()

form = cgi.FieldStorage()
event_id = form.getvalue("event_id")


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
    
    <div class="hero-wrap" style="background-image: url('images/bg_1.jpg');" data-stellar-background-ratio="0.5">
      <div class="overlay"></div>
      <div class="container">
        <div class="row no-gutters slider-text align-items-center justify-content-center" data-scrollax-parent="true">
          <div class="col-md-7 ftco-animate text-center" data-scrollax=" properties: { translateY: '70%' }">
             <p class="breadcrumbs" data-scrollax="properties: { translateY: '30%', opacity: 1.6 }"><span class="mr-2"><a href="index.html">Home</a></span> <span>campaigns</span></p>
            <h1 class="mb-3 bread" data-scrollax="properties: { translateY: '30%', opacity: 1.6 }">Campaign detail</h1>
          </div>
        </div>
      </div>
    </div>

    
    <section class="ftco-section">
      <div class="container">
      	<div class="row">
''')

if event_id:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="jeevankiran"
    )
    mycursor = mydb.cursor(dictionary=True)
    
    query = """
        SELECT e.id AS event_id, e.title AS event_title, e.description, e.objectives,
       e.yourhelp, e.contribution, e.impact, e.img,
       c.title AS campaign_title
FROM eventmaster e
JOIN campaignmaster c ON e.id = c.id
WHERE e.id = %s

    """
    mycursor.execute(query, (event_id,))
    ev = mycursor.fetchone()

    if ev:
        img_path = ev['img'] if ev['img'] else "default.jpg"
        print(f"""
        <div class="container text-center">
          <div class="image-box" style="background-image:url('eventuploads/{img_path}');"></div>
          <div class="details-box">
            <h2>{ev['event_title']}</h2>
            <h2><b>Campaign:</b><br> {ev['campaign_title']}</h2>
            <h2><b>Description:</b><br> {ev['description']}</h2>
            <h2><b> Our Objectives:</b><br> {ev['objectives']}</h2>
            <h2><b>How you can help:</b><br> {ev['yourhelp']}</h2>
            <h2><b>Contribution impact:</b><br> {ev['contribution']}</h2>
            <h2><b>Impact so far:</b><br> {ev['impact']}</h2>

            <a href="donate.py?event_id={ev['event_id']}" class="btn btn-success">Donate Now</a>
          </div>
        </div>
        """)
    else:
        print("<h3 style='color:red; text-align:center;'>Campaign not found!</h3>")
else:
    print("<h3 style='color:red; text-align:center;'>Invalid request!</h3>")

print("</body></html>")


print('''
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