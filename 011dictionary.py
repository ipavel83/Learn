#py3.7

d = {}
str = 'myKey'
str2 = 'myKey2'
print(d)

d[str]=1
d[str2]=5
d[str]+=2
d['another'] = 'string of string )'
print(d)

e =d.pop('another')
print(e)
print(d)

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