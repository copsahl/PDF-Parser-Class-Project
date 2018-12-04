'''
Main file combining everything into a working program.
'''

# # # # # # # # # # # # # # # # # # # # #
#                                       #
#   TODO: Implement lists for keywords  #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

import argparse
from parse import *
from dataOutput import *
from os import listdir, path

def main():

    print("\nParsing PDF Documents can produce false positives due to how PDF data is stored.")
    print("This program is accurate but you will find false positives.\n\n-----------------------------------------------------------------")

    # We must have a file or directory selected for the program to run
    if (args.file == None and args.dir == None) or args.key == None:
        parser.print_help()
        return 1

    args.key = args.key.split(',')
    for key in args.key:

        results = dict()

        # If we are supplied a file parse over the given file
        if args.file != None:
            tail = path.split(args.file)
            if not validatePDF(args.file):
                print("{} was not recognized as a valid PDF document.\nProgram Aborted.".format(args.file))
                print("Check to make sure the '.pdf' extention is attached to your file!")
                return 1
            else:
                pdfFile = open(args.file, 'rb')
                foundPages = keySearch(pdfFile, key)
                results[tail[1]] = keyOccurence(pdfFile, key, foundPages)
                writeResults(args.output, results)
        
        # If we are given a directory, walk the directory, grab pdf documents, and parse them.
        if args.dir != None:
            dirFiles = [x for x in listdir(args.dir) if validatePDF(x)]
            for f in dirFiles:
                if not validatePDF(f):
                    print("{} was not recognized as a valid PDF document.\nProgram Aborted.".format(args.file))
                    print("Check to make sure the '.pdf' extention is attached to your file!")
                    return 1
                else:
                    if ord(args.dir[-1]) == 92:
                        fullPath = args.dir + f
                    else:
                        fullPath = args.dir + chr(92) + f
                    pdfFile = open(fullPath, 'rb')
                    foundPages = keySearch(pdfFile, key)
                    results[f] = keyOccurence(pdfFile, key, foundPages)
                    writeResults(args.output, results)

        print("\n\nKEYWORD --> {}".format(key.upper()))
        print("\n'FILENAME'\n\tPAGE:OCCURENCES\n")
        printResults(results)

if __name__ == '__main__':

    examples = r'''example:

    python PDFparse.py -f myfile.pdf -k algorithm
    python PDFparse.py -d C:\ -k donkey -o myfile.txt
    python PDFparse.py -h
    '''

    # Command line arguments
    parser = argparse.ArgumentParser(description='PDF Document Parser', epilog=examples)
    parser.add_argument('-f', '--file', type=str, default=None, help="User specified PDF document to be parsed.")
    parser.add_argument('-d', '--dir', type=str, default=None, help="User specified directory. The parser will parse through all PDF files in the direcotry.")
    parser.add_argument('-k', '--key', type=str, default=None, help="User defined list of 1 or more keywords to parse for. REQUIRED")
    parser.add_argument('-o', '--output', type=str, default='parsedData.txt', help="Output file to store data. Default filename is 'parsedData.txt'")

    # Add output customization options for the parser
    args = parser.parse_args()

    main()
