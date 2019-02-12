#!/usr/bin/var python3
#py3.7

class PineTree:
    x = 0
    def __init__(self, color, height, pX=None):
        self.color = color
        self.height = height
        print('self.x before __init__:', self.x) #at first run: 0
        self.__class__.x+=1
        print('self.x:', self.x) #at first run: 1
        if pX != None:
            self.x = pX #if we have pX then shadow class variable "x" by it
    
    def __repr__(self):
        return '__repr__ for '+self.printName()
        
    def __str__(self):
        return '__str__ for '+self.printName()
    
    def printName(self):
        return f'PineTree id({id(self)})'+f' color:{self.color!r} {self.color}, height:{self.height}'
        
    def returnSelfX(self):
        return self.x
    
    @classmethod
    def returnClassX(cls):
        return cls.x
        
    @classmethod
    def makeYellowTree(cls, height, pX=None):
        return cls('Yellow', height, pX)
    
    @staticmethod
    def justSomeCalculation(x, y):
        return x + y
        
myTree = PineTree('green', 42)
print(PineTree.x, myTree.x,) #1 1
print(id(myTree))
print(f'plain conversion to string by {myTree}')
print(f'in list conversion to string going by {[myTree]}')
print(' ; ' , str(myTree), ' ; ' , repr(myTree))
myTree2 =PineTree('green', 42, 4)
print(PineTree.x, myTree.x, myTree2.x) #2 2 4
print('anonther tree for test: ',id(myTree2))
print('and first tree again: ',id(myTree))
myTree3 =PineTree('red', 25)
print(PineTree.x, myTree.x, myTree2.x, myTree3.x) #3 3 4 3
print('anonther tree for test: ',id(myTree3), myTree3)

myTree4 = PineTree.makeYellowTree(10,9)
myTree5 = PineTree.makeYellowTree(10)
#####Attention!
#Class method does NOT haveaccess to istance variables!
print(myTree4.returnSelfX(), myTree5.returnSelfX()) #PineTree.returnSelfX() - error because Class does not have self
print(PineTree.x, myTree4.x, myTree5.x)                                            #5 9 5 #five nine     five
print(PineTree.returnClassX(),  myTree4.returnClassX(), myTree5.returnClassX())    #5 5 5 #five !!!five!!! five

#just static method test
print(PineTree.justSomeCalculation(38, 11)) #49

print('Method binding start:')
#bind method to PineTree Class
def printBindedFunctionSelf(self):
        return f'Self id({id(self)})'+f' color:{self.color!r} {self.color}, height:{self.height}'
PineTree.wowMethod = printBindedFunctionSelf #class binding is easy
print(myTree2.wowMethod())
print(myTree4.wowMethod())

#bind new method ONLY to myTree4
from types import MethodType
myTree4.pr = MethodType(printBindedFunctionSelf, myTree4) #instance binding is ok too
print(myTree4.pr())
#print(myTree3.pr()) #AttributeError: 'PineTree' object has no attribute 'pr'


#Reusing other objects
class Person:
    def __init__(self, height):
        self.height = height
    def bio(self):
        print(f"I'm a person with height: {self.height}")

class Student(Person):
    def bio(self):
        Person.bio(self)
        print (f"I'm studying and my height is {self.height}")

class Cat:
    def __init__(self, height):
        self.height = height
    def icat(self,mew):
        print(f'I cat, my height is {self.height}',mew)
    def likeAMan(self):
        Person.bio(self)
        
p1 = Person(15)
p1.bio()
p2 = Student(32)
p2.bio()
Cat.icat(p1,'meeeow')
newCat = Cat(3)
newCat.icat('gfg')
newCat.likeAMan()