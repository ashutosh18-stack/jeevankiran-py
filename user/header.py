#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
form = cgi.FieldStorage()
id = form.getvalue("id")
print("Content-Type: text/html\n")
print(f'''
         <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
   <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css" integrity="sha512-5A8nwdMOWrSz20fDsjczgUidUBR8liPYU+WymTZP1lmY9G6Oc7HlZv156XqnsgNUzTyMefFTcsFH/tnJE/+xBg==" crossorigin="anonymous" referrerpolicy="no-referrer" />
<nav class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
    <div class="container">
      <a class="navbar-brand" href="index.html">Jeevankiran</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#ftco-nav" aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="oi oi-menu"></span> Menu
      </button>

      <div class="collapse navbar-collapse" id="ftco-nav">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item"><a href="index.py?id={id}" class="nav-link">Home</a></li>
          <li class="nav-item"><a href="about.py?id={id}" class="nav-link">About</a></li>
          <li class="nav-item"><a href="project.py?id={id}" class="nav-link">Project</a></li>
          <li class="nav-item"><a href="donate.py?id={id}" class="nav-link">Donate</a></li>
          <li class="nav-item"><a href="compaign.py?id={id}" class="nav-link">Compaigns</a></li>
          <li class="nav-item"><a href="contact.py?id={id}" class="nav-link">Contact</a></li>
          <li class="nav-item dropdown">
         <button class="btn btn-primary dropdown-toggle"
        style="background-color:#fd7e14; border-radius: 50px; width: 150px; height: 40px; padding: 0;"
        type="button" 
        id="profileDropdown" 
        data-bs-toggle="dropdown" 
        aria-expanded="false">
  <i class="fa fa-user" aria-hidden="true"style="margin-left:10px; margin-right:10px;"></i>My Profile
</button>

  <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="profileDropdown">
    ''')
print('''
<script>
      var fullname=localStorage.getItem("fullname");
      if(fullname=="" || fullname==null){
      document.write('<a href="usersignup.py" style="display: block; background-color:#fd7e14;" class="btn btn-primary rounded-pill py-2 px-3">Register</a>')
       
   document.write('<a href="userlogin.py" style="display: block; background-color:#fd7e14;" class="btn btn-primary rounded-pill py-2 px-3">Login</a>')
      }else{
         document.write('<a href="" style="display: block; background-color:#fd7e14;" class="btn btn-primary rounded-pill py-2 px-3" style="margin-right: 20px;">'+ fullname +'</a>')
       
        document.write('<a href="receipt.py" style="display: block; background-color:#fd7e14;" class="btn btn-primary rounded-pill py-2 px-3">Receipt</a>')
      
        document.write('<a href="userlogout.py" style="display: block; background-color:#fd7e14;" class="btn btn-primary rounded-pill py-2 px-3">Logout</a>')
      }
</script>
''')
print('''
      <script>
  var fullname = localStorage.getItem("fullname");
  if (fullname && fullname !== "") {
    document.write('<li><a href="editprofile.py" style="display: block; background-color:#fd7e14;" class="btn btn-primary rounded-pill py-2 px-3">Edit Profile</a></li>');
  }
</script>
''')
print('''
  </ul>
    
      </div>
    </div>
  </nav>
    <!-- END nav -->
''')
