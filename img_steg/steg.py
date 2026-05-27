from PIL import Image
import argparse

def main():
    parser = argparse.ArgumentParser(description='Script that hides a message or decrypts a message using least significant bit steganography with images')

    parser.add_argument('-d',action='store_true',help='Option Decrypt')
    parser.add_argument('-e',action='store_true',help='Option Encrypt')
    parser.add_argument('-f',required=True,type=str,help='File input path')
    parser.add_argument('-o',required=False,type=str,help='Output File path')
    parser.add_argument('-m', required=False, type=str,help='Hidden message you want to encrypt in the image')

    args = parser.parse_args()

    if not(args.d or args.e):
        parser.error('The script requires d or e flag')
    
    if (args.d):
        print("Decrypt")
    
    elif (args.e and args.o and args.m):
        print("Encrypt")

    else:
        parser.error("Incorrect usage, encryption requires a -e,-m,-o flags to run")

if __name__ == '__main__':
    main()