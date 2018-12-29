#py3.7
import collections

#############
ordDict1 = collections.OrderedDict(one=1, andTwo='Two', three=3, four=4)
print(ordDict1)
ordDict1['five']=5
ordDict1['two'] = 2
print(ordDict1)
print(ordDict1.keys())
print([(key, ordDict1[key]) for key in ordDict1.keys()])

justDict1 = {'something': 's', 'justAnother': 'ss2'}
##############
chainMap1 = collections.ChainMap(ordDict1, justDict1)
print(chainMap1)
print('from chainMap:', chainMap1['justAnother'])


############NamedTuple
tuple1 = ('one', 'andTwo', 3, 'four')
#del tuple1[1] #TypeError: 'tuple' object does not support item deletion
print('just tuple:', tuple1)

namedTup = collections.namedtuple('SomeTupleName_noSpaces','first second third fourth')
some1 = namedTup(*tuple1)
print('named tuple fields:', some1._fields)
print('named tuple name one way:    ', type(some1).__name__)
print('named tuple name other way:  ', some1.__class__.__name__) #but don't access the __class__ attribute directly, it's bad practice.
#print(dir(some1))
print(some1, 'Has length of', len(some1), 
		' and get it first element by 3 different ways: ', 
		some1[0], some1.first, getattr(some1, 'first'))
		
some2 = namedTup(first = 'q',second = 'w', third = 'e', fourth = 'r')
print(some2, 'Has length of', len(some2), 
		' and get it first element by 3 different ways: ', 
		some2[0], some2.first, getattr(some2, 'first')) 

from sys import getsizeof
print(getsizeof(tuple1), getsizeof(some1), getsizeof(some2))

##############Counter
stuff = collections.Counter()
lootDict = {'bread': 1, 'apple':1 }
stuff.update(lootDict) #Counter is adding elements not replacing it like simple dictionary
moreloot = {'towel':1, 'bread':3}
stuff.update(moreloot)
print(stuff)
stuff.update(lootDict)
print(stuff)
print(len(stuff), sum(stuff.values()))

################Python’s deque objects are implemented as doubly-linked lists
dq = collections.deque()
dq.append('first')
dq.append('sec')
dq.append('thiiird')
#dq.put('dfs') #AttributeError: 'collections.deque' object has no attribute 'put'
#print(dq.get()) #AttributeError: 'collections.deque' object has no attribute 'get'
print(dq)
print(dq.popleft())
print(dq)
print(dq.pop()) ########just usual pop right
print(dq)
print(dq.popleft())
#print(dq.popleft()) #IndexError: pop from an empty deque

#####this queue Python standard library is synchronized and provides locking semantics to support multiple concurrent producers and consumers.
#for mulitprocessing Queue see  Shared Job Queues - #from multiprocessing import Queue
from queue import Queue
qq = Queue()
qq.put('q')
qq.put('r')
qq.put('qfgd')
qq.put('a')
print(qq)
print(qq.get())
print(qq.get())
print(qq.get())
print(qq.get())
#print(qq.get()) #Blocks / waits forever...
