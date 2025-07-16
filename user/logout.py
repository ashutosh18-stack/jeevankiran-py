#!C:\Python312\python.exe
import cgi 
import cgitb 
cgitb.enable()
print("Content-Type: text/html\n")
print('''
<script>
 localStorage.clear();
 
 alert("logout Successfully!");
    location.href="login.py";
</script>
''')