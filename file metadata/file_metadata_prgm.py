#1.take in command line input and perform that action
import argparse
import PyPDF2

def decrypt(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        metadata = reader.metadata
        for key in metadata:
            print(f"{key} : {metadata[key]}")

def encrypt(file_path, metadata_key_name ,message,output_file_path):


    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()

        writer.append_pages_from_reader(reader)

        metadata = reader.metadata 
        #returns metadata dictionary
        metadata.update({metadata_key_name : message})
        writer.add_metadata(metadata)

        with open(output_file_path,"wb") as output_file_path:
            writer.write(output_file_path)

        print("Message hidden succesfully ")





def main():
    parser = argparse.ArgumentParser(description= "script that append user defined data to a pdf's metadata or reads a pdf's metadata")

    parser.add_argument('-d',action= 'store_true',help='Option decrypt')
    parser.add_argument('-e', action = 'store_true', help = "Option encrypt")
    parser.add_argument('-f', required=True,type=str,help='file path')
    parser.add_argument('-o',required=False,type=str,help='output file path')
    parser.add_argument('-mn',required=False,type=str,help='metadata key name')
    parser.add_argument('-m',required=False,type=str,help = "The hidden message that you want to hide in the pdf's metadata")

    args = parser.parse_args()

    if not(args.d or args.e):
        parser.error("the script requires either a -e or -d flag")

    if args.d:
        decrypt(args.f)
    elif args.f:
        if (args.o and args.mn and args.m):
            encrypt(args.f,args.mn,args.m,args.o)
        else:
            parser.error("The script requires the -o,-mn,-m flags to run the encryption function")


if __name__ == "__main__":
    main()
