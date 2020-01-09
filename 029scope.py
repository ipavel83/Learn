#py3.7 #https://docs.python.org/3/tutorial/classes.html#scopes-and-namespaces-example

def scopeFunction():
    
    def localScope():
        test = 'localScope'
        
    def nonlocalScope():
        nonlocal test
        test = 'nonlocalFuction'
    
    def globalScope():
        global test
        test = 'globalFunction'
    
    test = 'scope'
    localScope()
    print('localScope()', test) #localScope() scope
    
    nonlocalScope()
    print('nonlocalScope()', test)  #nonlocalScope() nonlocalFuction 
    
    globalScope()
    print('globalScope()', test)    #globalScope() nonlocalFuction #####it changed in global scope

print('text variable after:')
scopeFunction()
print('scopeFunction()', test)  #scopeFunction() globalFunction

#def both():
#    def GlobalNonlocal():
#        global test
#        nonlocal test ########SyntaxError: name 'test' is nonlocal and global
#        test = 'nonlocalGlobal'
#    GlobalNonlocal()
#    print('GlobalNonlocal()', test)
#both()
#print('both()', test)