#!C:\Python312\python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Context-Type:text/html\n")
form=cgi.FieldStorage()
#print(form)
name=form.getvalue("name")
#print(name)
email=form.getvalue("email") 
#print(email)
subject=form.getvalue("subject")
#print(subject)
message=form.getvalue("message")
#print(message)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="jeevankiran")
mycursor = mydb.cursor()
query =f"""INSERT INTO `contact`(`name`, `email`, `subject`, `message`) VALUES ('{name}','{email}','{subject}','{message}')"""
#print(query)
mycursor.execute(query)
mydb.commit()
print(f'''<script>alert("Message Send Successfully!");
    location.href="../contact.py";
    </script>''')


