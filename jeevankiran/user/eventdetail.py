#!C:/Python312/python.exe
import cgi
import cgitb
cgitb.enable()
import mysql.connector
import header

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
mycursor = mydb.cursor(dictionary=True)

# Fetch all events
query = "SELECT * FROM eventmaster"
mycursor.execute(query)
result = mycursor.fetchall()

print("Content-Type: text/html\n")
print('''
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Our Events</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f9f9f9;
            margin: 0;
            padding: 0;
        }
        .wrapper {
            width: 90%;
            margin: 30px auto;
        }
        .page-heading {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 20px;
            text-align: center;
            color: #333;
        }
        .event-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
        }
        .event-card {
            background: #fff;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            overflow: hidden;
            transition: 0.3s;
        }
        .event-card:hover {
            transform: translateY(-5px);
        }
        .event-card img {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }
        .event-card .content {
            padding: 15px;
        }
        .event-card h3 {
            margin: 0 0 10px;
            color: #fd7e14;
            font-size: 18px;
        }
        .event-card p {
            font-size: 14px;
            color: #555;
            margin: 5px 0;
            white-space: pre-line;
        }
        .btn-view {
            display: inline-block;
            margin-top: 10px;
            padding: 8px 15px;
            background: #fd7e14;
            color: #fff;
            border: none;
            text-decoration: none;
            border-radius: 5px;
            font-size: 14px;
            transition: 0.3s;
        }
        .btn-view:hover {
            background: #e96a00;
        }
    </style>
</head>
<body>
    <div class="wrapper">
        <div class="page-heading">
            <i class="fas fa-calendar-alt"></i> Our Events
        </div>
        <div class="event-container">
''')

# Loop to display all events
for row in result:
    id = row['id']
    title = row['title']
    description = row['description']
    objectives = row['objectives']
    yourhelp = row['yourhelp']
    contribution = row['contribution']
    impact = row['impact']
    image = row['eventImage'] if row['eventImage'] else "images/default.jpg"

    print(f'''
        <div class="event-card">
            <img src="uploads/{image}" alt="{campaign}">
            <div class="content">
                <h3>{campaign}</h3>
                <p><b>Description:</b> {description}</p>
                <p><b>Objectives:</b> {objectives}</p>
                <p><b>How You Can Help:</b> {yourhelp}</p>
                <p><b>Contribution:</b> {contribution}</p>
                <p><b>Impact:</b> {impact}</p>
                <a href="eventdetails.py?id={id}" class="btn-view">View More</a>
            </div>
        </div>
    ''')

print('''
        </div>
    </div>
</body>
</html>
''')
