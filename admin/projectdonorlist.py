#!C:/Python312/python.exe
import cgi
import cgitb
import header
import mysql.connector
import os
cgitb.enable()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jeevankiran"
)
mycursor = mydb.cursor(dictionary=True)
query = "SELECT * FROM package_payment"
mycursor.execute(query)
results = mycursor.fetchall()

# HTML Output
print('''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Project List</title>
  <link rel="stylesheet" href="style/ngomasterlist.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
  <style>
    .ngo-list-container {
      max-width: 1300px;
      margin: auto;
      background-color: #ffffff;
      padding: 25px;
      border-radius: 10px;
      box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    }

    table {
      width: 100%;
      border-collapse: collapse;
    }

    th, td {
      text-align: left;
      padding: 12px 9px;
      border-bottom: 1px solid #ddd;
      vertical-align: top;
      word-wrap: break-word;
      word-break: break-word;
      white-space: pre-wrap;
    }

    th {
      background-color: #2980b9;
      color: white;
      text-transform: uppercase;
    }

    td.message {
      max-width: 250px;
    }

    .project-img-group {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }

    .project-img-group img {
      width: 60px;
      height: 60px;
      object-fit: cover;
      border-radius: 6px;
      border: 1px solid #ddd;
    }

    td.actions a {
      margin-right: 6px;
      color: #444;
      font-size: 10px;
    }
  </style>
</head>
<body>
  <div class="ngo-list-container">
    <h2><i class="fas fa-list"></i>Project Donated List</h2>
    <table>
      <thead>
        <tr>
          <th>ID</th> 
      <th>USER ID</th> 
          <th>NAME</th>
          <th>EMAIL</th>
        
          <th>ITEM</th>
          <th>QUANTITY</th>
          <th>AMOUNT</th>
      <th>PAY STATUS</th>
      <th>TRANSACTION</th>
          <th>MESSAGE</th>
        </tr>
      </thead>
      <tbody>
''')

# Loop through data
for x in results:
    packageid = x['donated_id']
    userid =x['user_id']
    name = x['user_name']
    email = x['user_email']
    package = x['package_item']
    quantity = x['quantity']
    amount = x['amount']
    payment=x['payment_status']
    transaction=x['transaction_id']
    message = x['message']

    print(f'''
      <tr>
        <td>{packageid}</td>
         <td>{userid}</td>
        <td>{name}</td>
        <td>{email}</td>
        <td>{package}</td>
        <td>{quantity}</td>
        <td>{amount}</td>
           <td>{payment}</td>
              <td>{transaction}</td>
        <td class="message">{message}</td>
      </tr>
    ''')

print('''
      </tbody>
    </table>
  </div>
</body>
</html>
''')
