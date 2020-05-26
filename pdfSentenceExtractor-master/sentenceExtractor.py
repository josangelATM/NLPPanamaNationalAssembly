#Library imports
from sys import argv
import os
#file imports
from extractor import pdfSentenceExtractor

def getFilesName(directory):
    '''
    We will return files[2]
    because os.walk returns a tuple
    with root, dirs, and files. 
    But we only need files.
    '''
    for files in os.walk(directory):
        return files[2]
    


def sentenceExtractor():
    sentences = []
    pdfs_directory = argv[1]
    files = getFilesName(pdfs_directory)
    for file in files:
        file_path = '.\\'+pdfs_directory+'\\'+file
        print('Extracting: '+file_path)
        #Extraction
        sentences = sentences + pdfSentenceExtractor(file_path)
    
    file1 = open("SentencesOutput.txt","a") 
    for sent in sentences:
        file1.write(sent)
    file1.close() 
    

if __name__ == "__main__":
    sentencelist = sentenceExtractor()
    #print(sentencelist)
