#1.import PyPDF2
#2.read incoming file
#3.copy the pages from the incoming file to a new file (copy the page data)
#4. Copying the metadata
#5. Adding the new metadata object(key:value), to the copied metadata 
#6.save the new file with new metadata containing the hidden msg

import PyPDF2

pdfpath = "Boring_Data.pdf"

with open(pdfpath, "rb") as file:
    reader = PyPDF2.PdfReader(file)
    writer = PyPDF2.PdfWriter()

    writer.append_pages_from_reader(reader)

    #message object (key, value)
    key = '/Key'
    message = 'this is hidden message in metadata'

    metadata = reader.metadata 
    #returns metadata dictionary
    metadata.update({key:message})
    writer.add_metadata(metadata)

    with open('hidden.pdf',"wb") as output_file:
        writer.write(output_file)

    print("Message hidden succesfully ")

