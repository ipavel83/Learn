#py3.7

def strFromOperation(operation,a, b):
	return f'{operation} {a} and {b} result'

def add(a, b):
	return a + b

def chooseBiggerOrZero(a, b):
	if a > b:
		return a
	elif a < b:
		return b
	else:
		return 0

def logOperarion(operation, a, b):
	print(strFromOperation(operation.__name__, a, b))
	return operation(a, b)

print(logOperarion(add, 7,8))
print(logOperarion(chooseBiggerOrZero, 7,8))
print(chooseBiggerOrZero(1, 2))
print(chooseBiggerOrZero(4, 5))
print(chooseBiggerOrZero(4, 4))

def Плюс(переменнаяА, переменнаяБ): #https://stackoverflow.com/questions/17043894/what-unicode-symbols-are-accepted-in-python3-variable-names
	return переменнаяА + переменнаяБ

print(logOperarion(Плюс, 7,8))

def noReturn():
	print('no return - return:')
print(noReturn())
#assert noReturn() == None

def explicitNone():
	print('explicit none:')
	return None
print(explicitNone())