#!/usr/bin/env python3
#py3.7

def retDeco(func1):
	def dec(text2):
		return 'start '+func1(text2)+' end'
	return dec

@retDeco
def funText(text):
	return ''.join([text[i].upper() if i%2 == 0 else text[i].lower() for i in range(len(text))])
	
	
a= funText('hello everyone!')
print(a)