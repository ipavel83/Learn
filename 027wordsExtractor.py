#py3.7

import sys

if len(sys.argv) < 3:
    print('use at least 2 parameters: fileNameToExtract, lettersToFind')
    sys.exit()
scriptName = sys.argv[0]
filenameToExtract = sys.argv[1]
lettersToFind = sys.argv[2]
textToExtract = ''
splited=[]
result = ''
if __name__ == '__main__':
    try:
        with open(filenameToExtract) as txt:
            textToExtract =txt.read()
            splited = textToExtract.split()
            check = set(lettersToFind)
            for w in splited:
                if all([x in check for x in w]):
                    result = result+w+' '
            #print(splited)
            #print(result)
        
        with open('extractedFrom_'+filenameToExtract, 'w') as txt2:
            txt2.write(result)
        print(f'extracted {len(result.split())} words and writen them to {"extractedFrom_"+filenameToExtract}')
    except IOError:
        print(f"can't open file {filename}")

