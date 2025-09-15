#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
# import header
# print('''

#       <!-- Content -->
#       <section class="content">
#         <h2>Welcome to the Admin Dashboard</h2>
#         <p>This is your main content area.</p>
#       </section>
#     </div>
#   </div>
# </body>
# </html>
# ''')
form = cgi.FieldStorage()
admin_id = form.getvalue("admin_id")

if not admin_id:
    print("""
    <script>
        alert("Access Denied: Please login first!");
        window.location.href = "login.py";
    </script>
    """)
    exit()