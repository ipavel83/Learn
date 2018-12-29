#py3.7 
from sys import argv
script, first, second, third = argv #if no 3 additional params to script then error: ValueError: not enough values to unpack (expected 4, got 1)

print (f"Arguments of called script: {argv}, and it length: {len(argv)}")
print("script called:", script)
print("first arg is:", first)
print("second arg is:", second)
print("third arg is:", third)