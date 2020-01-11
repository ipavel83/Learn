#py3.8
from inspect import currentframe, getframeinfo
frameinfo = getframeinfo(currentframe())
print (f'{frameinfo.filename}, {frameinfo.lineno}')


var42 = 42

print (f'codeline: {getframeinfo(currentframe()).lineno} ::')

print ('number to binary string:')

print (var42, bin(var42))
print (var42, bin(var42)[2:])

print (var42, f"{var42:#b}")

print (var42, f"{var42:b}") #for now (2019) its will be main method

print (0, f"{0:b}")
print (255, f"{255:b}")
print (-1, f"{-1:b}")
print (-42, f"{-42:b}")

print (f'codeline: {getframeinfo(currentframe()).lineno} ::')
print ('old way using format: ',var42, "{0:b}".format(var42))

print ()

def toBin(val): #throws exception on negative numbers
    arr = []
    if val< 0:
        raise ValueError ('to convert to binary using this function value should be >= 0')
    while val > 1:
        arr.append(val % 2)
        val = val // 2
    arr.append(val % 2)
    return ''.join([str(x) for x in list(reversed(arr))])

def toBinRecur(num): #fails on negative numbers like -42
    s = ''
    if num > 1: 
        s = toBinRecur(num // 2) 
    return s + str(num % 2) 

def tryRunAndPrintCustomBinary(func):
    print ('function to test:', func.__name__)
    print (var42, func(var42))
    print (0, func(0))
    print (1, func(1))
    print (4, func(4))
    print (255, func(255))
    try:
        print (-1, func(-1))
    except Exception as e:
        print (e, str(e))
    try:
        print (-42, func(-42))
    except Exception as e:
        print (e, str(e))
    print()
    
print (f'codeline: {getframeinfo(currentframe()).lineno} ::')
print ('now cutom functions:')
print ()
tryRunAndPrintCustomBinary(toBin)
tryRunAndPrintCustomBinary(toBinRecur)

