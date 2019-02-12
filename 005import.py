#py3.7 
from sys import argv
script, first, second, third = argv #if no 3 additional params to script then error: ValueError: not enough values to unpack (expected 4, got 1)

#myLabelModule = __import__('123drawSplitedColorLabelClass')        #import from fileName started with number

#TODO test Absolute and Relative Imports #https://docs.python.org/2.5/whatsnew/pep-328.html


print (f"Arguments of called script: {argv}, and it length: {len(argv)}")
print("script called:", script)
print("first arg is:", first)
print("second arg is:", second)
print("third arg is:", third)

##########relative import
helloModule = __import__('001hello')
print('imported relatively:', helloModule.a, helloModule.b, helloModule.c)
