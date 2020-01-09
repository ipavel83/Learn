#py3.7

class VeryBase(object):
    classvar ='1somevar'
    classvarToOverride ='2somevar'
    def __init__(self):
        self.instvar ='3somevar'
        self.instvarToOverride ='4somevar'
    def method(self):
        print('5method')
    def methodToOverride(self):
        print('6methodToOverride')
        
        
class WillOverride(VeryBase):
    classvarToOverride = '7Overriden_classVar'
    classvarSomeOther = '8someotherVarOfChildClass'   
    def childMethod(self):
        print('9childMethod')  
    def methodToOverride(self):
        print('9Overriden_methodToOverride')

print('differences:')
test = WillOverride()
baseDir = dir(VeryBase)
childDir = dir(WillOverride)
for m in baseDir:
    method = getattr(VeryBase, m)
    if method != getattr(WillOverride, m):
        print (f'{m} is {type(method)} and different in VeryBase and WillOverride')
print('child unique:')
childDir = dir(WillOverride)
for m in childDir:
    method = getattr(WillOverride, m)
    if m not in baseDir:
        print(f'{m} is {type(method)} and unique to WillOverride')
