#Module usage:
# 1) set "pathname" to directory where need to acquire file paths
# 2) call makeListsOfFiles()

import os

pathname = ""
fileList = None # global, will be initialized in makeListsOfFiles #[]
pathList = None #[]
fileFullPathList = None #[]

def makeListsOfFiles():
    global fileList
    fileList = []
    global pathList
    pathList = []
    global fileFullPathList
    fileFullPathList = []
    for root, dirs, files in os.walk(pathname):
        for file in files:
            fileList.append(file)
            pathList.append(root)
            fileFullPathList.append(root + "\\" + file)
            
def writeListToFile(fileName, list):
    with open(fileName, "w", encoding="utf-8") as fileToWrite:
        for item in list:
            fileToWrite.write(item + "\n")    
    
#if module was executed as standalone write lists to files and print fileList and paths 
if __name__ == "__main__": 
    #import sys
    from sys import argv
    pathname = os.path.dirname(argv[0]) 
    
    makeListsOfFiles()
    makeListsOfFiles()
    
    writeListToFile("exFileList.txt", fileList)    
    writeListToFile("exFilePathList.txt", fileFullPathList)
    
    #def openAndPrintAllFiles(list):
    #    for item in list:
    #        print(open(item).read())
    #openAndPrintAllFiles(fileFullPathList)
    
    for i in range(len(fileList)):
        print(fileList[i], pathList[i])
        
    

    
#fileList.sort() #changes list inplace
#print("N. of files", len(fileList))
#fileListSorted = sorted(fileList)
#writeListToFile(writeNameSorted, fileListSorted)    
        
# see all the methods of os
# print(*dir(os), sep=", ")
#os.system("lista_file.txt") #exFileList.txt
#os.system("lista_file_ordinata.txt") #exFileListSorted.txt
#os.system("filePathList.txt") #exFilePathList.txt
