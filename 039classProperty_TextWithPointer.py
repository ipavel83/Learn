#py3.7

class TextWithPointer(object):
    
    def __init__(self, text):
        self.text = text;
        self._position = 0;
        
    @property
    def charAtCurrentPointer(self):
        return self.text[self._position];
    
    @property
    def pointer(self):
        return self._position;
        
    @pointer.setter
    def pointer(self, value):
        ##if (value > len(self.text)) || (value < 0):
            #raise IndexError(f"value {value} is not pointing in text (range 0 - {len(self.text)})")
        self._position = value
        

def printTextClass(textClass):
    print(textClass)
    print("text:", someText.text)
    print("pointer:", someText.pointer)
    print("_position:", someText._position)
    print("charAtCurrentPointer:", someText.charAtCurrentPointer)

someText = TextWithPointer("some text to fiddle with")
printTextClass(someText)
print(someText.text[0], someText.text[1], someText.text[2], someText.text[3])

someText.pointer =2
printTextClass(someText)

someText.pointer =3
printTextClass(someText)




