import os
from PyPDF2 import PdfReader
import csv

# Initialize variables
InvoiceNo = None
Price = None
Issuer = None
Date = None

# Loop through PDF files
for filename in os.listdir("."):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(".", filename)

        # creating a pdf reader object 
        reader = PdfReader(pdf_path)

        # Loop through all pages and extract text
        for page in reader.pages:
            text = page.extract_text()

            # Write the text to a CSV file
            with open("bolt.csv", "a") as pdfconvert:
                pdfconvert.write(text + "\n")

        # Process CSV data for each PDF
        with open("bolt.csv", "r") as text_file, open("finaldata.csv", "a", newline="\n") as finaldata:
            csv_writer = csv.writer(finaldata)
            lines = text_file.readlines()
            printed_lines = set()

            for line in lines:
                stripped_line = line.strip()

                if "(RON)" in stripped_line and "including" in stripped_line and stripped_line not in printed_lines:
                    Price = stripped_line
                    printed_lines.add(Price)
                    Price = Price.replace("T otal  including  V A T  (RON): ","")

                if "Invoice  no." in stripped_line and stripped_line not in printed_lines:
                    InvoiceNo = stripped_line
                    printed_lines.add(InvoiceNo)
                    InvoiceNo = InvoiceNo.replace("Invoice  no.  ", "")

                if "Issued  on  behalf  of  " in stripped_line and stripped_line not in printed_lines:
                    Issuer = stripped_line
                    Issuer = Issuer.replace("Issued  on  behalf  of  ", "")
                    Issuer = Issuer.replace("by  Bolt  Operations  OÜ  /  V ana - L õuna  15,  T allinn  10134,", "")
                    printed_lines.add(Issuer)

                if "Date:  " in stripped_line and stripped_line not in printed_lines:
                    Date = stripped_line
                    Date = Date.replace("Date:  ", "")
                    printed_lines.add(Date)

            # Check if all information is available before writing to CSV
            if all([InvoiceNo, Price, Issuer, Date]):
                csv_data = [
                    ["InvoiceNo", "Price", "Issuer", "Date"],
                    [InvoiceNo, Price, Issuer, Date]
                ]
                csv_writer.writerows(csv_data)


os.remove("bolt.csv")
