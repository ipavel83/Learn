#py3.7

integers = range(5)
squared=(i*i for i in integers)
plus3= (i + 3 for i in squared)
print( *(plus3) )

def repeaterGenerator(value, maxReps):
	count = 0
	while True:
		if count >= maxReps:
			return
		yield value[count]
		count +=1


for item in repeaterGenerator('HelloGen',4):
	print(item)
	
#difference with listComprehensions is that Generator expression return values on demand
#Generator expression not constructing list object 
# list comprh [], gen expr ()
iterExpr = ( 'iterExprLikeListComprehens' for i in range(4) )
for item in iterExpr:
	print(item)
		

###########class iterator
		
class BoundedRepIterator:
	def __init__(self, value, maxRepeats):
		self.value = value;
		self.maxRepeats = maxRepeats
		self.count = 0
	
	def __iter__(self):
		return self
	
	def __next__(self):
		if self.count >=self.maxRepeats:
			raise StopIteration
		self.count +=1
		return self.value

brep = BoundedRepIterator('HelloCount', 8)
for item in brep:
	print(item)

brep = BoundedRepIterator('wHelloCount', 8)
iterator = iter(brep)
while True:
	try:
		item = next(iterator)
	except StopIteration:
		break
	print('while', item)
	
###############very basic class iterator with NO stop, just for understanding:
class Repeater:
	def __init__(self, value):
		self.value = value
		
	def __iter__(self):
		return RepeaterIterator(self)

	
class RepeaterIterator:
	def __init__(self, source):
		self.source = source
		
	def __next__(self):
		return self.source.value

repeater = Repeater('HelloFor')
i = 0
for item in repeater:
	if i>4:
		break
	print(item)
	i+=1

repeater = Repeater('HelloWhile')
iterator = repeater.__iter__()
i = 0
while i < 5:
	item = iterator.__next__()
	print(item)
	i+=1
	
