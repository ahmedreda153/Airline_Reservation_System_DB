from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
import DataBase_connection

def generate_pdf_report():
    # Count the number of aircrafts grouped by type
    DataBase_connection.cursor.execute("SELECT AIRCRAFT_TYPE AS Type, COUNT(*) AS Number_of_Aircraft FROM AIRCRAFT GROUP BY AIRCRAFT_TYPE")
    aircraft_data = DataBase_connection.cursor.fetchall()
    # Select the aircraft with the highest capacity
    DataBase_connection.cursor.execute("SELECT MAX(CAPACITY) AS Capacity FROM AIRCRAFT")
    max_aircraft_capacity = DataBase_connection.cursor.fetchall()
    # Display all flights order by price in ascending order
    DataBase_connection.cursor.execute("SELECT FLIGHT_NUM AS Flight_Number, SOURCE_LOCATION AS Source, DESTINATION_LOCATION AS Destination, DEPARTURE_TIME AS Departure_Time, ARRIVAL_TIME AS Arrival_Time, PRICE AS Price FROM FLIGHT ORDER BY PRICE")
    flight_data = DataBase_connection.cursor.fetchall()
    # Display the customer who booked the most tickets in descending order
    DataBase_connection.cursor.execute("SELECT PERSON.FNAME, PERSON.LNAME, COUNT(TICKET.TICKETID) AS Number_of_Tickets FROM PERSON, TICKET WHERE PERSON.ID = TICKET.ID GROUP BY PERSON.FNAME, PERSON.LNAME ORDER BY Number_of_Tickets DESC")
    # Create a new PDF document
    document = SimpleDocTemplate("report.pdf", pagesize=letter)

    # Define styles
    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    heading_style = styles["Heading2"]
    normal_style = styles["Normal"]
    # normal_style.fontSize = 14
    table_style = TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.skyblue),  # Header background color
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),  # Header text color
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),  # Center alignment for all cells
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),  # Header font
        ("FONTSIZE", (0, 0), (-1, 0), 12),  # Header font size
        ("BOTTOMPADDING", (0, 0), (-1, 0), 10),  # Header bottom padding
        ("BACKGROUND", (0, 1), (-1, -1), colors.lightgrey),  # Content background color
        ("GRID", (0, 0), (-1, -1), 1, colors.black),  # Grid lines
        ("FONTSIZE", (0, 1), (-1, -1), 10),  # Content font size
        ("BOTTOMPADDING", (0, 1), (-1, -1), 5),  # Content bottom padding
    ])

    # Create the report for the PDF
    report = []

    # Add report title
    title = Paragraph("Airline Reservation System Report", title_style)
    report.append(title)
    report.append(Paragraph("<br/><br/>", normal_style))

    intro = Paragraph("Welcome to SAJAH, a simple and user-friendly airline reservation system that makes your travel experience easier. Our system lets you easily create an account and log in. Users can update their profile information. User can update profile info easily, Administrators can add, update and delete aircraft and flight details. Customers can access a list of available flights based on specific criteria, book, cancel, and even change flight class.", normal_style)
    report.append(intro)
    report.append(Paragraph("<br/><br/>", normal_style))

    # Number of aircraft per type
    report.append(Paragraph("Number of Aircraft per Type:", heading_style))
    report.append(Paragraph("<br/>", normal_style))

    aircraft_type_data = [["Aircraft Type", "Aircraft Count"]]
    for type in aircraft_data:
        aircraft_type_data.append([type.Type, str(type.Number_of_Aircraft)])

    aircraft_type_table = Table(aircraft_type_data, style=table_style)
    report.append(aircraft_type_table)
    report.append(Paragraph("<br/><br/><br/><br/><br/>", normal_style))

    # Maximum aircraft capacity
    report.append(Paragraph("Maximum Aircraft Capacity:", heading_style))
    report.append(Paragraph("<br/>", normal_style))

    max_aircraft_capacity_table = Table([["Maximum Aircraft Capacity"], [str(max_aircraft_capacity[0].Capacity)]], style=table_style)
    report.append(max_aircraft_capacity_table)
    report.append(Paragraph("<br/><br/><br/><br/><br/><br/><br/><br/>", normal_style))

    # Flight details sorted by price
    report.append(Paragraph("Flight Details Sorted by Price:", heading_style))
    report.append(Paragraph("<br/>", normal_style))

    flight_data_table_data = [["Flight Number", "Source", "Destination", "Departure Time", "Arrival Time", "Price"]]
    for flight in flight_data:
        flight_data_table_data.append([flight.Flight_Number, flight.Source, flight.Destination, str(flight.Departure_Time), str(flight.Arrival_Time), str(flight.Price)])

    flight_data_table = Table(flight_data_table_data, style=table_style)
    report.append(flight_data_table)
    report.append(Paragraph("<br/><br/><br/><br/><br/>", normal_style))

    # Most customer booked flight
    report.append(Paragraph("Most Customer Booked Flight:", heading_style))
    report.append(Paragraph("<br/>", normal_style))

    most_customer_booked_flight_table_data = [["Name", "Number of Tickets"]]
    for customer in DataBase_connection.cursor.fetchall():
        most_customer_booked_flight_table_data.append([customer.FNAME + " " + customer.LNAME, str(customer.Number_of_Tickets)])
        
    most_customer_booked_flight_table = Table(most_customer_booked_flight_table_data, style=table_style)
    report.append(most_customer_booked_flight_table)
    report.append(Paragraph("<br/><br/>", normal_style))

    # Build the PDF document
    document.build(report)