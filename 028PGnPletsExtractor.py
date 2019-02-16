#py3.7

import sys
from decimal import Decimal
from collections import Counter

if len(sys.argv) < 3:
    print('use at least 2 parameters: fileNameToExtract, NumberPletsToExtract')
    sys.exit()
scriptName = sys.argv[0]
filenameToExtract = sys.argv[1] #filenameToExtract = 'pg100.txt'
numPlets = int(sys.argv[2]) #numPlets = 1
textToExtract = ''
splited=[]
result = Counter()
if __name__ == '__main__':
    try:
        with open(filenameToExtract) as txt:
            for line in txt:
                splited = line.split()
                wordToExtract =splited[1]
                count= Decimal(splited[2])
                npletsInWord=len(wordToExtract) - numPlets + 1
                for i in range(npletsInWord): #TODO modificate from 1 letter to numPlets
                    #strOnlyLetters[1:3]) #cut start at index 1 and end before 3
                    result.update({wordToExtract[i:i+numPlets]: count})
                #print(wordToExtract, splited[2], count)
            #
            #check = set(lettersToFind)
            #for w in splited:
            #    if all([x in check for x in w]):
            #        result = result+w+' '
            #print(splited)
            #print(result)
        
        with open(f'extracted{numPlets}pletsFrom_'+filenameToExtract, 'w') as txt2:
            sortRes = sorted(result.items(), key=lambda x:x[1], reverse=True)
            i=0
            #print(len(sortRes))
            for k, v in sortRes: #for k, v in result.items():
                txt2.write(f'{k} {v}')
                if i<(len(sortRes)-1):
                    txt2.write('\n')
                i+=1
            #txt2.write(str(result))
        print(f'extracted {len(result)} {numPlets}plets and writen them to {"extractedFrom_"+filenameToExtract}')
    except IOError:
        print(f"can't open file {filename}")