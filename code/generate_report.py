from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
import DataBase_connection

def generate_pdf_report():
    # groub by category name and count books in each category
    DataBase_connection.cursor.execute("SELECT MANUFACTURER AS CategoryName, COUNT(*) AS BookCount FROM AIRCRAFT GROUP BY MANUFACTURER")
    category_data = DataBase_connection.cursor.fetchall()
    # get most 3 borrowed books from borrow table
    # DataBase_connection.cursor.execute()
    # book_data = DataBase_connection.cursor.fetchall()
    # # get top 3 users who borrowed most books
    # DataBase_connection.cursor.execute()
    # user_data = DataBase_connection.cursor.fetchall()
    # Create a new PDF document
    doc = SimpleDocTemplate("report.pdf", pagesize=letter)

    # Define styles
    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    heading_style = styles["Heading2"]
    normal_style = styles["Normal"]
    table_style = TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),  # Header background color
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),  # Center alignment for all cells
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),  # Header font
        ("FONTSIZE", (0, 0), (-1, 0), 12),  # Header font size
        ("BOTTOMPADDING", (0, 0), (-1, 0), 10),  # Header bottom padding
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),  # Content background color
        ("GRID", (0, 0), (-1, -1), 1, colors.black),  # Grid lines
        ("FONTSIZE", (0, 1), (-1, -1), 10),  # Content font size
        ("BOTTOMPADDING", (0, 1), (-1, -1), 5),  # Content bottom padding
    ])

    # Create the story (content elements) for the PDF
    story = []

    # Add report title
    title = Paragraph("Airline Reservation System Report", title_style)
    story.append(title)
    story.append(Paragraph("<br/><br/>", normal_style))

    # Add category details to the PDF
    story.append(Paragraph("Books of each Category:", heading_style))
    story.append(Paragraph("<br/>", normal_style))

    category_table_data = [["Category", "Book Count"]]
    for category in category_data:
        category_table_data.append([category.CategoryName, str(category.BookCount)])

    category_table = Table(category_table_data, style=table_style)
    story.append(category_table)
    story.append(Paragraph("<br/><br/>", normal_style))

    # Add book details to the PDF
    # story.append(Paragraph("Top 3 Borrowed Books:", heading_style))
    # story.append(Paragraph("<br/>", normal_style))

    # book_table_data = [["Book Title", "Borrow Count"]]
    # for book in book_data:
    #     book_table_data.append([book.BookTitle, str(book.BorrowCount)])

    # book_table = Table(book_table_data, style=table_style)
    # story.append(book_table)
    # story.append(Paragraph("<br/><br/>", normal_style))

    # # Add user details to the PDF
    # story.append(Paragraph("Top 3 Users who borrowed books:", heading_style))
    # story.append(Paragraph("<br/>", normal_style))

    # user_table_data = [["First Name", "Last Name", "Borrow Count"]]
    # for user in user_data:
    #     user_table_data.append([user.FirstName, user.LastName, str(user.BorrowCount)])

    # user_table = Table(user_table_data, style=table_style)
    # story.append(user_table)

    # Build the PDF document
    doc.build(story)