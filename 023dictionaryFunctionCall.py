#py3.7

def functionCalc(operation, arg1, arg2):
    d = {'add': lambda x, y: x + y , 
        'sub': lambda x, y: x - y, }
    d['mul'] = lambda x, y: x * y
    d['div'] = lambda x, y: arg1 / arg2 #using external arg1 and arg2 in lambda
    #print(d) #for logging
    return d.get(operation, lambda x, y: None)(arg1, arg2) #error if just "pass" in lambda, so return None
    
print( functionCalc('add', 3, 7) )
print( functionCalc('adddddd', 3, 7) )
print( functionCalc('sub', 3, 7) )
print( functionCalc('mul', 3, 7) )
print( functionCalc('div', 3, 7) )
print( functionCalc('div', 8, 4) )

