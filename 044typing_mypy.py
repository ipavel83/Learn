#py3.8
#All errors in this file happen ONLY in static analisys utils like MyPy
#This file should execute just fine :)

from typing import NoReturn, List, Union, Optional

def noRet() -> NoReturn:
    #annotation NoReturn used for functions that should NOT return any values
    #also can be used for showing that function throws an EXCEPTION
    print('no return function:')
    return 'this is should be ERROR' #should make MyPy typing error
    
print(noRet())

