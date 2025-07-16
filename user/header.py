#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
print("Content-Type: text/html\n")
print('''
<nav class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
    <div class="container">
      <a class="navbar-brand" href="index.html">Jeevankiran</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#ftco-nav" aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="oi oi-menu"></span> Menu
      </button>

      <div class="collapse navbar-collapse" id="ftco-nav">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item"><a href="index.py" class="nav-link">Home</a></li>
          <li class="nav-item"><a href="about.py" class="nav-link">About</a></li>
          <li class="nav-item"><a href="project.py" class="nav-link">Project</a></li>
          <li class="nav-item"><a href="donate.py" class="nav-link">Donate</a></li>
          <li class="nav-item"><a href="compaign.py" class="nav-link">Compaigns</a></li>
          <li class="nav-item"><a href="contact.py" class="nav-link">Contact</a></li>
          <li class="nav-item dropdown">
''')
print('''
<script>
      var fullname=localStorage.getItem("fullname");
      if(fullname=="" || fullname==null){
      document.write('<a href="signup.py" style="border-radius: 50px; background-color:#fd7e14; margin-right:20px;" class="btn btn-primary rounded-pill py-2 px-3">Register</a>')
       
   document.write('<a href="login.py" style="border-radius: 50px; background-color:#fd7e14;margin-right:-55px;" class="btn btn-primary rounded-pill py-2 px-3">Login</a>')
      }else{
         document.write('<a href="" style="border-radius: 50px; background-color:#fd7e14; margin-right:20px;" class="btn btn-primary rounded-pill py-2 px-3" style="margin-right: 20px;">'+ fullname +'</a>')
       
        document.write('<a href="logout.py" style="border-radius: 50px; background-color:#fd7e14; margin-right:-55px;" class="btn btn-primary rounded-pill py-2 px-3">Logout</a>')
      }
</script>
''')
print('''
          
        </li>
        </ul>
      </div>
    </div>
  </nav>
    <!-- END nav -->
''')
