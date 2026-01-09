#!C:/Python312/python.exe
import cgi, cgitb
cgitb.enable()
import mysql.connector
import sys, io
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from datetime import datetime

# Get donation_id from query string
form = cgi.FieldStorage()
donation_id = form.getvalue("donation_id")

if not donation_id:
    print("Content-Type: text/html; charset=utf-8\r\n")
    print("<h2 style='color:red;text-align:center;'>Donation ID Missing!</h2>")
    sys.exit()

try:
    # Connect to DB
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="jeevankiran"
    )
    cursor = db.cursor(dictionary=True)

    # Fetch donation details
    cursor.execute("""
        SELECT donation_id, name, email, amount,
               razorpay_order_id, razorpay_payment_id,
               payment_date
        FROM donate_payment
        WHERE donation_id=%s AND payment_status='paid'
    """, (donation_id,))
    donation = cursor.fetchone()

    if not donation:
        print("Content-Type: text/html; charset=utf-8\r\n")
        print("<h2 style='color:red;text-align:center;'>Donation Not Found or Payment Pending!</h2>")
        sys.exit()

    # Build PDF in memory
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    left = 20 * mm
    top = height - 20 * mm
    line_height = 8 * mm

    # Header
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(colors.darkgreen)
    c.drawCentredString(width / 2, top, "The Leafy Spot")
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.black)
    c.drawCentredString(width / 2, top - 6 * mm, "Donation Receipt")

    # Divider line
    c.setLineWidth(1)
    c.line(left, top - 8 * mm, width - left, top - 8 * mm)

    # Metadata
    y = top - 18 * mm
    c.setFont("Helvetica-Bold", 10)
    c.drawString(left, y, "Receipt No.:")
    c.setFont("Helvetica", 10)
    c.drawString(left + 35 * mm, y, str(donation.get("donation_id", "")))

    y -= line_height
    c.setFont("Helvetica-Bold", 10)
    c.drawString(left, y, "Date:")
    c.setFont("Helvetica", 10)
    pd = donation.get("payment_date")
    if isinstance(pd, datetime):
        pd_str = pd.strftime("%Y-%m-%d %H:%M:%S")
    else:
        pd_str = str(pd) if pd else ""
    c.drawString(left + 35 * mm, y, pd_str)

    # Donor Info
    y -= 12 * mm
    c.setFont("Helvetica-Bold", 10)
    c.drawString(left, y, "Donor Name:")
    c.setFont("Helvetica", 10)
    c.drawString(left + 35 * mm, y, donation.get("name", ""))

    y -= line_height
    c.setFont("Helvetica-Bold", 10)
    c.drawString(left, y, "Email:")
    c.setFont("Helvetica", 10)
    c.drawString(left + 35 * mm, y, donation.get("email", ""))

    # Donation Details Table
    y -= 12 * mm
    c.setFont("Helvetica-Bold", 10)
    c.drawString(left, y, "Amount (INR):")
    c.setFont("Helvetica", 10)
    c.drawString(left + 35 * mm, y, str(donation.get("amount", "")))

    y -= line_height
    c.setFont("Helvetica-Bold", 10)
    c.drawString(left, y, "Razorpay Order ID: ")
    c.setFont("Helvetica", 10)
    c.drawString(left + 35 * mm, y, donation.get("razorpay_order_id", ""))

    y -= line_height
    c.setFont("Helvetica-Bold", 10)
    c.drawString(left, y, "Razorpay Payment ID: ")
    c.setFont("Helvetica", 10)
    c.drawString(left + 40 * mm, y, donation.get("razorpay_payment_id", ""))

    # Footer note
    y -= 20 * mm
    c.setFont("Helvetica-Oblique", 9)
    c.drawString(left, y, "This is a computer-generated receipt. No signature required.")
    y -= 8 * mm
    c.drawString(left, y, "Thank you for your contribution to The Leafy Spot.")

    # Organization contact
    y -= 12 * mm
    c.setFont("Helvetica", 8)
    c.drawString(left, y, "The Leafy Spot | Address | City | Phone: +91-XXXXXXXXXX")

    c.showPage()
    c.save()
    buffer.seek(0)
    pdf_data = buffer.read()

    # Stream PDF to browser
    out = sys.stdout.buffer
    filename = f"receipt_{donation['donation_id']}.pdf"
    out.write(b"Content-Type: application/pdf\r\n")
    out.write(f"Content-Disposition: attachment; filename=\"{filename}\"\r\n\r\n".encode("utf-8"))
    out.write(pdf_data)
    out.flush()

except Exception as e:
    print("Content-Type: text/html; charset=utf-8\r\n")
    print(f"<h2 style='color:red;text-align:center;'>Error: {e}</h2>")
    sys.exit()

finally:
    try:
        cursor.close()
        db.close()
    except:
        pass
