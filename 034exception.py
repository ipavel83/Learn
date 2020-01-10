#py3.7

try:
    print(len(None))
except BaseException as e:
    print (e, ' _ ', type(e), ' _ ', dir(e))    #object of type 'NoneType' has no len()  _  <class 'TypeError'> , #######output of dir#######

#except ValueError as e ##to use short exception var e
#except (RuntimeError, TypeError, NameError): if 3 different type in one
####### BADBADBAD except RuntimeError, TypeError:  ---- is OLD syntax and EQUIVOLENT to except RuntimeError as TypeError: which is NOT what YOU want

    
print('Now run tryEvalOperation')

def tryEvalOperation(operation, *args):
    print()
    try:
        if len(args)<1:
            print (operation, eval(operation))
    except ValueError:
        print(ValueError) #####
    except TypeError as t:
    
        print('TypeError happen: ', t) #TypeError happen:  object of type 'NoneType' has no len()
        print(t.args) #("object of type 'NoneType' has no len()",)
        
        print(TypeError) #<class 'TypeError'>
        print(TypeError.args) #<attribute 'args' of 'BaseException' objects> ####without as is just class <class 'ZeroDivisionError'>
        
    except ZeroDivisionError:
        print(ZeroDivisionError) 
    except:
        print('exception for anything')
    finally:
        print('finally')
    
    
tryEvalOperation('1/2')
tryEvalOperation('1/0') #ZeroDivisionError
tryEvalOperation('len(None)') #TypeError
    
    
# except Exception as inst:
#     print type(inst)     # the exception instance
#     print inst.args      # arguments stored in .args
#     print inst           # __str__ allows args to be printed directly
    
#also from: https://docs.python.org/2/tutorial/errors.html#handling-exceptions
#import sys
#
#try:
#    f = open('myfile.txt')
#    s = f.readline()
#    i = int(s.strip())
#except IOError as e:
#    print "I/O error({0}): {1}".format(e.errno, e.strerror)
#except ValueError:
#    print "Could not convert data to an integer."
#except:
#    print "Unexpected error:", sys.exc_info()[0]
#    raise
    
    
#for with (predefined clean up) look at:
#https://docs.python.org/2/tutorial/errors.html#predefined-clean-up-actions
#014with.py
#


