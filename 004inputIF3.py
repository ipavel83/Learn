#py3.7
print('input something:')
what=input()
strWhat = str(what)
print( what, type(what), len(what),'and converted to string:', strWhat, type(strWhat), len(strWhat))

#python.org FAQ: Is there an equivalent of C’s ”?:” ternary operator?
#something = [on_true] if [expression] else [on_false]
a = 'longer than 2 chars' if len(strWhat)>2 else 'shorter than 3 chars'

print('You typed',strWhat)
print(f'you typen something {a}')
print('You again inputed -',input('input something again!'))
#for more info type in terminal: C:\Python\Python37-32\python -m pydoc input 