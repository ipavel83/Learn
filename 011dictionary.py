#py3.7

print( {True: 'yes', 1: 'no', 1.0: 'maybe'} ) #prints {True: 'maybe'} 
#dictionary creation overwrites values of same key, key is not updated due optimization
#bool is subclass of int, so True is 1
print(True == 1 == 1.0 ) #True
print( (hash(True), hash(1), hash(1.0)) ) #(1, 1, 1)

####back to dict :)
d = {}
print(d)
str = 'myKey'
str2 = 'myKey2'
d[str]=1
d[str2]=5
d[str]+=2
d['another'] = 'string of  *&^%'
d['myKey5']=0
print(d)
e =d.pop('another')
print(e)
print(d)

######combining dictionarys
d2 = {'wow': 8, 'myKey5': 99, 'myKey4':44}
print(d2)
dComb = {}
dComb.update(d)
dComb.update(d2)
print('one way to combine dictionary:       ', dComb)
print('another way to combine dictionary: ', {**d, **d2})


###### access if keys not in dict
#one way
try:
    print(d['noSuchKey'])
except KeyError:
    print ('Key error happen, but it was catched')
#and another
print(d.get('keyNotInDict', 'default If Not foutd'))

###sort by value using lambda
dTupSorted= sorted(d.items(), key=lambda x: x[1])
dfromSorted = dict(dTupSorted)
print('sorted by value tuple from dict:',dTupSorted, 'And dict from it:', dfromSorted)

###### check if key is in dict:
if str in d:
    print (f'{str} is in {d}')
else:
    print (f'ERR {str} not found is in {d}')
if 'myKey2' in d:
    print (f'myKey2 is in {d}')
else:
    print (f'ERR myKey2 not found is in {d}')
if 'another' not in d:
    print('another not in d')
else:
    print('ERR another is FOUND in d')
    
#also can check item using method get
#dict.get(key[, default])
if d.get("test") != None:
    print("Yes 'test' key exists in dict")    
else:
    print("No 'test' key does not exists in dict") 

print('loop1')
for i in d:
    print(i, d[i])
    
print('loop2')
for k, v in d.items():
    print(k, v)
    
d.clear()
print(d)