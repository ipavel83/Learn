#!/usr/bin/var python3
#py3.7
import inspect

def printArgs(one, two=2, *args, **kwargs):
    print(f'\nprint {inspect.currentframe().f_code.co_name}:')
    print(one)
    print(two)
    print(args)
    print(kwargs)

#printArgs() #TypeError: printArgs() missing 1 required positional argument: 'one'
#printArgs(,) #TypeError: printArgs() missing 1 required positional argument: 'one'
printArgs('1_call',)
printArgs('2_call','Two',)
printArgs('3_call','Two','three',)
printArgs('4_call','Two',par1='three',)
#printArgs('5_call','Two',par1='three','fourt',) #SyntaxError: positional argument follows keyword argument
printArgs('5_call','Two','fourt', par1='three',)
printArgs('5_call','andFive','Two','fourt', par1='three',)
#printArgs('5_call', ,'andFive','Two','fourt', par1='three',) #SyntaxError: invalid syntax
printArgs('5_call', None ,'andFive','Two','fourt', par1='three',)
printArgs('5_call', '' ,'andFive','Two','fourt', par2= 'seven' ,par1='three',par3='eight')
printArgs(1, 2, 3, 4, 9, 8, 7, par2=222, par1=1, par3=3)

dict = { 'hi':'hii' , 'nice':'niiice',}
#printArgs(*[1,2,3,4,5,6,7,], hi='hii', **dict) #TypeError: printArgs() got multiple values for keyword argument 'hi'
printArgs(*[1,22,3,4,5,6,7,], hi2='hii', **dict)

print('genexpr:')
genexpr = (x * x for x in range(5))
print(genexpr)
print(list(genexpr))
print(list(genexpr)) #genexpr now empty: []
#TODO find out more about generator expressions and posibility of its rewind(reuse)

#for now just redeclare generator expression
genexpr = (x * x for x in range(5))
printArgs(*genexpr)