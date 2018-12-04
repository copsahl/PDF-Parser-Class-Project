'''
Functions for parsing PDF documents in specific ways
'''
# # # # # # # # # # # # # # # # # # # # #
#                                       #
#   TODO: MAKE PARSING MORE ACCURATE!   #
#   TODO: Implement multiprocesing      #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

import re
import PyPDF2

def validatePDF(file):
    '''Make sure the user is passing us a PDF document. If it is valid, return true'''
    valid = False
    validate = re.findall(r"([a-zA-Z0-9]*\.{1}pdf)", file) # This regular expression allows file such as test.txt.pdf which can result in imporper fild handling
    if validate:
        valid = True
    return valid

def keySearch(pdfFileObject, key):
    '''Parse through PDF file and return the pages that the keyword or phrase is found on'''
    pages = list()
    pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
    numOfPages = pdfReader.numPages
    for page in range(0, numOfPages):
        try:
            pageObj = pdfReader.getPage(page)
            text = pageObj.extractText()
            if key.lower() in text.lower():
                pages.append(page + 1)
        except:
            continue
    return pages

def keyOccurence(pdfFileObject, key, pageList):
    '''Parse through given pages pages, and find each occurance of the word return dictionary'''
    occurences = {}
    pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
    for page in pageList:
        count = 0
        pageObj = pdfReader.getPage(page - 1)
        text = pageObj.extractText()

        words = text.split()
        
        for word in words:
            if key.lower() == word.lower():
                count += 1
        

        occurences[str(page)] = count

    return occurences
