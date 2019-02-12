#py3.7
import os

def makeListsOfFiles(DirPath): #from 010fileDirs.py
    fileFullPathList = []
    for root, dirs, files in os.walk(DirPath):
        for file in files:
            fileFullPathList.append(root + "\\" + file)
    return fileFullPathList
    
def filterText(text):
    def filterOnlyPrintable(str):
        return filter(lambda x: x in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~ \t\n\r\x0b\x0c', str) #import string #string.printable
    def filterOnlySeenableAndSpace(str):
        return filter(lambda x: x not in '\t\n\r\x0b\x0c', str) #characters taken from end of string.printable
        
        filtered1 = filterOnlyPrintable(text)
        filtered2 = filterOnlySeenableAndSpace(filtered1)
        return filtered2
    
def fileReadFiltered(filePath):
    txt = open(filePath)
    return filterText(txt.read())
    
    
def combineNPletDicts(dict1, dict2):
    ret = dict1.copy()
    for i in dict2:
        if i in ret:
            ret[i]+=dict2[i]
        else:
            ret[i]=dict2[i]
    return ret
    
def nPlets(text, n): #from 012nPletsFromString.py
    ret = {}
    if n<1: return ret
    
    for i in range(len(text)-n+1):
        cut = text[i:i+n]
        if cut in ret:
            ret[cut] += 1
        else:
            ret[cut] = 1
        #print(cut)
    return ret
    
#########################################################################
import unittest

class TestStringMethods(unittest.TestCase):
    def test_combineDicts(self):
        duDict1 = {'a ': 1, ' s': 2, 'sa': 3, 'am': 2, 'mp': 1}
        duDict2 = {'sa': 1, ' b': 3, 'am': 5, 'nd': 3, ' a': 1 ,'ot': 2}
        duDict3 = combineNPletDicts(duDict1, duDict2)
        self.assertEqual(duDict3, {'a ': 1, ' s': 2, 'sa': 4, 'am': 7, 'mp': 1, ' b': 3, 'nd': 3, ' a': 1, 'ot': 2})
        self.assertEqual(duDict1['am'], 2)
        self.assertEqual(duDict2['am'], 5)

        
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == "__main__":
    from sys import argv
    if len(argv)>1 and argv[1] == 'runTests':
        unittest.main(argv=['FakeArgvToRemoveErrorsIfCalledWithParams'])
    else:
        print('Runned just like a program without "runTests" parameter, argv: ', argv)
