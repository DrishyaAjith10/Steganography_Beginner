import PyPDF2
pdfpath = "hidden.pdf"

with open(pdfpath, "rb") as file:
    reader = PyPDF2.PdfReader(file)

    metadata = reader.metadata
    for key in metadata:
        print(f"{key} : {metadata[key]}")