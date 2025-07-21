#!C:/Python312/python.exe
import cgi
import os
import mysql.connector
import cgitb
cgitb.enable()
print("Content-Type: text/html\n")

form=cgi.FieldStorage()
# print(form)
item=form.getvalue('item')
# print(item)