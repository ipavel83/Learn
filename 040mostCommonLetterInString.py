import operator

countDict = dict.fromkeys([x for x in range(ord("a"),ord("z")+1)], 0)
def resetDict():
    countDict.update({x:0 for x in range(ord("a"),ord("z")+1)})

def updateLetterCount(letter: str):
    temp = ord(letter.lower())
    if temp in countDict:
        countDict.update({temp: countDict[temp]+1})

def mostCommonLetter(text: str) -> str:
    for letter in text:
        updateLetterCount(letter)
    maxLetter = max(countDict.items(), key=operator.itemgetter(1))[0]
    #print(maxLetter, chr(maxLetter))
    #print(countDict)
    #print(text, maxLetter, chr(maxLetter))
    resetDict()
    return chr(maxLetter)

if __name__ == '__main__':
    #print(countDict)
    #print(chr(122))

    assert mostCommonLetter("Hello World!") == "l"
    assert mostCommonLetter("How do you do?") == "o"
    assert mostCommonLetter("One") == "e"
    assert mostCommonLetter("Aabbc!") == "a"
    assert mostCommonLetter("cAaBBb!!!!") == "b"
    assert mostCommonLetter("abcdefg") == "a"
    assert mostCommonLetter("a" * 9999 + "b" * 5000) == "a"