import os
from PyPDF2 import PdfReader

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

# Initialize variables
InvoiceNo = None
Price = None
Issuer = None

# Process CSV data
with open("bolt.csv", "r") as text_file, open("finaldata.csv", "a") as finaldata:
    lines = text_file.readlines()
    printed_lines = set()

    for line in lines:
        stripped_line = line.strip()

        if "(RON)" in stripped_line and "including" in stripped_line and stripped_line not in printed_lines:
            Price = stripped_line
            print(Price)
            printed_lines.add(Price)
            finaldata.write(Price.replace("T otal  including  V A T  (RON): ", "") + "\n")

        if "Invoice  no." in stripped_line and stripped_line not in printed_lines:
            InvoiceNo = stripped_line
            print(InvoiceNo)
            printed_lines.add(InvoiceNo)
            finaldata.write(InvoiceNo.replace("Invoice  no.  ", "") + "\n")

        if "Issued  on  behalf  of  " in stripped_line and stripped_line not in printed_lines:
            Issuer = stripped_line
            print(Issuer)
            printed_lines.add(Issuer)
            Issuer = Issuer.replace("Issued  on  behalf  of  ", "")
            Issuer = Issuer.replace("by  Bolt  Operations  OÜ  /  V ana - L õuna  15,  T allinn  10134,", "")
            finaldata.write(Issuer + "\n")


os.remove("bolt.csv")