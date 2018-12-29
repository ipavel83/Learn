#py3.7

theInts = [1, 2, 3]
theStrings = ['a one', 'a two', 'a three', 'a four']
varLc = 'lc'
theMixed = [1, 'la', 2, 'lb', 3, varLc]

for num in theInts:
	print('Pyhonic way:', num)

for i, item in enumerate(theInts):
	print(f'Pyhonic way: {i} {item}')
	
for i in range(len(theInts)):
	print('not very pythonic way of loop through items:', i, theInts[i])

#for i in range(a, n, s):
#	... # in java it like:
#for (int i = a; i < n; i += s) { 
# ... }

for i in range(0,len(theMixed)):
	print('theMixed:',theMixed[i])
for i in range(0,len(theMixed),2):
	print('theMixed with step of 2:',theMixed[i])
for i in range(0,len(theMixed),3):
	print('theMixed with step of 3:',theMixed[i])
	

print('list comprehensions')
######list comprehensions is VERY Pythonic
#values = [ EXPRESSION for ITEM in COLLECTION if CONDITION]

#can also be expressed not pythonic way like:
#	values = []
#	for item in collection:
#		if condition:
#			values.append(expression)
from numbers import Number
print([x * 10 for x in theMixed if isinstance(x, Number) ])
print( *( x * 100 for x in theMixed if isinstance(x, Number) ) ) # * is needed to print generator object
#without * print will be: #<generator object <genexpr> at 0x034C29B0>
#also can do same with range:
print(*range(8))
cDict = {x: x * x + 10 for x in range(5)}
print(cDict)
	
######while used very rarely, useful if loop is going forever. So, almost never
print('while almost always not pythonic:')
i = 0
while i < 10: #use while for loops that runs forever - so almost never (LearnP3 HW p126)
	print(i)
	i+=2

	