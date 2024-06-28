from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

# Data for the e-commerce fashion purchase receipt
DATA = [
    ["Date", "Item", "Category", "Price (Rs.)"],
    ["26/06/2024", "Men's Leather Jacket", "Apparel", "5,999.00/-"],
    ["26/06/2024", "Women's Silk Scarf", "Accessories", "1,299.00/-"],
    ["26/06/2024", "Unisex Sunglasses", "Accessories", "2,499.00/-"],
    ["Sub Total", "", "", "9,797.00/-"],
    ["Discount", "", "", "-1,000.00/-"],
    ["Total", "", "", "8,797.00/-"],
]

# Creating a Base Document Template of page size A4
pdf = SimpleDocTemplate("fashion_receipt.pdf", pagesize=A4)

# Standard stylesheet defined within reportlab itself
styles = getSampleStyleSheet()

# Fetching the style of Top level heading (Heading1)
title_style = styles["Heading1"]

# 0: left, 1: center, 2: right
title_style.alignment = 1

# Creating the paragraph with the heading text and passing the styles of it
title = Paragraph("Fashion Store Receipt", title_style)

# Creating a Table Style object and defining the styles row wise
style = TableStyle(
    [
        ("BOX", (0, 0), (-1, -1), 1, colors.black),
        ("GRID", (0, 0), (4, 4), 1, colors.black),
        ("BACKGROUND", (0, 0), (3, 0), colors.darkblue),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("BACKGROUND", (0, 1), (-1, -1), colors.lightgrey),
    ]
)

# Creating a table object and passing the style to it
table = Table(DATA, style=style)

# Building the actual PDF by putting together all the elements
pdf.build([title, table])
