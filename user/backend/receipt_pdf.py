#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
import mysql.connector
import io
import sys
import os
import datetime

# IMPORTANT: do NOT re-wrap sys.stdout here because we will write binary to stdout.buffer
form = cgi.FieldStorage()
donation_id = form.getvalue("donation_id")

# Simple error HTML helper
def html_error(msg):
    print("Content-Type: text/html; charset=utf-8\r\n")
    print(f"<html><body><h2>{msg}</h2></body></html>")
    sys.exit(0)

if not donation_id:
    html_error("Error: donation_id not provided.")

# Connect to DB — adjust credentials if needed
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="jeevankiran"
    )
except Exception as e:
    html_error("Database connection error: " + str(e))

cursor = mydb.cursor(dictionary=True)
cursor.execute("SELECT * FROM package_payment WHERE donated_id=%s", (donation_id,))
donation = cursor.fetchone()
if not donation:
    html_error("Donation record not found.")

# Try to import reportlab; instruct user if missing
try:
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
    from reportlab.lib.units import mm
except ImportError:
    html_error("reportlab library not installed. Run: pip install reportlab")

# Build PDF in-memory
buffer = io.BytesIO()
c = canvas.Canvas(buffer, pagesize=A4)
width, height = A4

# Header
c.setFont("Helvetica-Bold", 18)
c.drawCentredString(width / 2, height - 20 * mm, "JeevanKiran NGO")
c.setFont("Helvetica", 12)
c.drawCentredString(width / 2, height - 26 * mm, "Donation Receipt")

# Divider
c.line(20 * mm, height - 28 * mm, width - 20 * mm, height - 28 * mm)

# Metadata
left = 20 * mm
y = height - 40 * mm

c.setFont("Helvetica-Bold", 10)
c.drawString(left, y, "Receipt No.:")
c.setFont("Helvetica", 10)
c.drawString(left + 35 * mm, y, str(donation.get("donated_id", "")))

y -= 8 * mm
c.setFont("Helvetica-Bold", 10)
c.drawString(left, y, "Date:")
c.setFont("Helvetica", 10)
pd = donation.get("payment_date")
if isinstance(pd, datetime.datetime):
    pd_str = pd.strftime("%Y-%m-%d %H:%M:%S")
else:
    pd_str = str(pd) if pd else ""
c.drawString(left + 35 * mm, y, pd_str)

# Donor info
y -= 12 * mm
c.setFont("Helvetica-Bold", 10)
c.drawString(left, y, "Donor Name:")
c.setFont("Helvetica", 10)
c.drawString(left + 35 * mm, y, donation.get("user_name", ""))

y -= 8 * mm
c.setFont("Helvetica-Bold", 10)
c.drawString(left, y, "Email:")
c.setFont("Helvetica", 10)
c.drawString(left + 35 * mm, y, donation.get("user_email", ""))

# Donation details
y -= 12 * mm
c.setFont("Helvetica-Bold", 10)
c.drawString(left, y, "Package Item:")
c.setFont("Helvetica", 10)
c.drawString(left + 35 * mm, y, donation.get("package_item", ""))

y -= 8 * mm
c.setFont("Helvetica-Bold", 10)
c.drawString(left, y, "Quantity:")
c.setFont("Helvetica", 10)
c.drawString(left + 35 * mm, y, str(donation.get("quantity", "")))

y -= 8 * mm
c.setFont("Helvetica-Bold", 10)
c.drawString(left, y, "Amount (INR):")
c.setFont("Helvetica", 10)
c.drawString(left + 35 * mm, y, str(donation.get("amount", "")))

y -= 12 * mm
c.setFont("Helvetica-Bold", 10)
c.drawString(left, y, "Transaction ID: ")
c.setFont("Helvetica", 10)
c.drawString(left + 35 * mm, y, str(donation.get("transaction_id", "")))

# Footer / note
y -= 20 * mm
c.setFont("Helvetica-Oblique", 9)
c.drawString(left, y, "This is a computer generated receipt. No signature required.")
y -= 8 * mm
c.drawString(left, y, "Thank you for your contribution to JeevanKiran NGO.")

# Optional: organization address or contact (customize)
y -= 18 * mm
c.setFont("Helvetica", 8)
c.drawString(left, y, "JeevanKiran NGO | Address line 1 | City | Phone: +91-XXXXXXXXXX")

c.showPage()
c.save()

buffer.seek(0)
pdf_data = buffer.getvalue()

# Save PDF file to server (so user can download later from dashboard)
receipts_dir = os.path.join(os.getcwd(), "receipts")   # make sure web server can serve this folder
os.makedirs(receipts_dir, exist_ok=True)
filename = f"receipt_{donation_id}.pdf"
file_path = os.path.join(receipts_dir, filename)

try:
    with open(file_path, "wb") as f:
        f.write(pdf_data)
except Exception as e:
    # do not fail the download — but log or show a small warning; we will still stream the PDF
    pass

# Update DB so receipt_path points to the saved file (relative path)
rel_path = f"receipts/{filename}"
try:
    cursor.execute("UPDATE package_payment SET receipt_path = %s WHERE donated_id = %s", (rel_path, donation_id))
    mydb.commit()
except Exception:
    pass

# Stream PDF to browser with proper headers
# Write headers as bytes then the binary PDF
out = sys.stdout.buffer
out.write(b"Content-Type: application/pdf\r\n")
out.write(f"Content-Disposition: attachment; filename=\"{filename}\"\r\n".encode("utf-8"))
out.write(b"\r\n")
out.write(pdf_data)
out.flush()

# close db
cursor.close()
mydb.close()
