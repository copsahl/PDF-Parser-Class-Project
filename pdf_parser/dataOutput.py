'''
Functions for outputting user specified data about the pdf document
'''

# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#   TODO: Allow different output methods  #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #

def printResults(resultsDictionary):
    '''Print out nested dictionary and only display results with entries'''
    #TODO: Fix function to for cases where 'myfile.pdf:{'53':0,'72':0}'
    # this problem will still print out the filename but won't print out the pages because they are false positives. 
    
    for k,v in resultsDictionary.items():
        if len(v) != 0:
            print(k)
        else:
            continue
        for x,y in v.items():
            if y != 0:
                print('\t\n{}:{}'.format(x,y), end="")

def writeResults(filename, resultsDictionary):
    '''Write out results to a text file'''

    textFile = open(filename, 'a+') 
    for k,v in resultsDictionary.items():
        if len(v) != 0:
            textFile.write(k)
        else:
            continue
        for x,y in v.items():
            if y != 0:
                textFile.write('\t\n{} : {}'.format(x,y))

