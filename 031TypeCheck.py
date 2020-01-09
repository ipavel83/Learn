#py3.7

import types    #from types import MethodType, FunctionType

#i = 2
#type(i) is int #not recommended
#isinstance(i, int)

class SomeClass:
    def fun():
        pass

print('what type is SomeClass.fun?', type(SomeClass.fun)) #<class 'function'>

if isinstance( SomeClass.fun, types.MethodType):    #False
    print('fun is types.MethodType')
    
if isinstance( SomeClass.fun, types.FunctionType): #True
    print('fun is types.FunctionType')
  
print()
def justFun():
    pass
print('what type is justFun?', type(justFun))
if isinstance( justFun, types.FunctionType):    #True
    print('justFun is types.FunctionType')