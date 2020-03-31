# PDF-Parser

A command line tool to make parsing data from multiple PDF documents faster written in python 3.6.3

You can scan individual files with the *-f* option. Or you can scan whole directories of PDF documents with the *-d* command.

## Usage

python PDFparse.py -f <*filename*> -k <*keyword*> -o <*output file name*>

python PDFparse.py -d <*path to directory*> -k <*keyword*> -o <*output file name*>

## Examples

Individual File:

    python PDFparse.py -f ImpracticalPython.pdf -k algorithm -o results.txt

![Individual File](pics/output1.png?raw=true")

Scanning Directory - In the picture, the *comparison.pdf* did not have the keyword. *ImpracticalPython.pdf* did.:

    python PDFparse.py -d <directoryPath> -k program -o results.txt

![Whole Directory](pics/output2.png?raw=true")

## Modules
* argparse
* os.listdir, os.path
* re
* PyPDF2 `pip install PyPDF2`

