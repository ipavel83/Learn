#py3.7

def nPlets(text, n):
	ret = {}
	if n<1: return ret
	
	for i in range(len(text)-n+1):
		cut = text[i:i+n]
		if cut in ret:
			ret[cut] += 1
		else:
			ret[cut] = 1
		#print(cut)
	return ret

def filterAllThatLess(dict, n):
	ret = {}
	for x in dict:
		if dict[x]>=n:
			ret[x] = dict[x]
	return ret

st = '''a sample, and another(one)? And another one.{
 sasaAnass =!
 }
 
 text Ends'''
#one = nPlets(st,1)
#print(one)
two = nPlets(st,2)
print(two)
two2 = filterAllThatLess(two,2)
print(two2)
three = nPlets(st,3)
print(three)
three2 = filterAllThatLess(three,2)
print(three2)
#four = nPlets(st,4)

import re
pattern = r'\w+|[^\w\s]+'
flags=re.UNICODE | re.MULTILINE | re.DOTALL
regexp = re.compile(pattern, flags)
tReg =  regexp.findall(st)
print(tReg)
#TODO try .finditer - https://docs.python.org/2/library/re.html#finding-all-adverbs-and-their-positions

listStr = []
listPos = []
for m in re.finditer(pattern, st):
	listStr.append(m.group(0))
	listPos.append(m.start())
	print (f'{m.start()}-{m.end()}: {m.group(0)}')
	
listZip = list(zip(listStr,listPos))
print(listZip)
listincl1 = [(listStr[i], listPos[i]) for i in range(len(listStr))]
print(listincl1)
listincl2 = [[listStr[i], listPos[i]] for i in range(len(listStr))]
print(listincl2)
