#py3.7
intVar1 = 12
print(type(intVar1),intVar1)
strIntVar1 =str(intVar1)
print(len(strIntVar1)) #length strIntVar1 is 2

print(type(strIntVar1),strIntVar1,'just text', sep=':-:', end= '; ')
print(str(intVar1)+strIntVar1, end= '; \n\n')

strIntVar1+='abc'
print("text and variable inside it {} and {} - will be printed".format(intVar1,strIntVar1))
print(f"python 3.6 formated text and variable inside it {intVar1} and {strIntVar1}")
strVarOption ='VarA'
strResult= (f'strResult= text1 with {strVarOption} ' f'text2 with {intVar1} '
f'text with {strVarOption}' f'text with {strVarOption} '
f'text with {strIntVar1}')
strVarOption = 'b'
print(strResult)
print()

print ('%02d-%02d: %s' % (15, 23, 'HELLO')) #Python2 way to format strings
print()

formater = '{} {} and {} one more {} and maybe {}'
#print(formater.format(1,2,'3m',4)) #format must have enougth elements# IndexError: tuple index out of range
print(formater.format(1,2,'3m',4,'empty text'))
formater = '{} {} and {}'
print(formater.format(1,2,'3m',4,'empty text')) #format more elements is OK - #output: 1 2 and 3m

print()
i = 10
s = '10'
print(f'fstring with repr inside for int - {i!r}, for string - {s!r}')  #https://www.python.org/dev/peps/pep-0498/#abstract


print()
print('NOW WE SLICE:')
strOnlyLetters = "This is only letters"
#slicing syntax [START:STOP:STEP]
print(1,strOnlyLetters, strOnlyLetters[3]) #letter at 3 index is 's'
print(2,strOnlyLetters[1:3]) #cut start at index 1 and end before 3
print(3,strOnlyLetters[2:]) #cut start at index 2
#if we need to slice to end with step, just omit STOP:
print(4,strOnlyLetters[2::3]) #cut start at index 2 with step3
print(5,strOnlyLetters[::-1])
print(6,strOnlyLetters[8::-1]) #cut start at index 2 with step-1
#print(7,strOnlyLetters[len(strOnlyLetters)-1::-1]) #not pythonic 5
print(8,strOnlyLetters[len(strOnlyLetters)-1::-2])
#print(strOnlyLetters[len(strOnlyLetters)]) #IndexError: string index out of range
print(9,strOnlyLetters[100::-1]) #no IndexError, buy why?
print()

#slice can be used in LIST
#especialy useful to clean LIST without destroying it: del LISTVAR[:]
#LISTVAR[:] is also shalow copy of LISTVAR
#LISTVAR[:] is LISTVAR #returns False because we create shaloow but still copy

print("text\nNext strint\nAnd next one\n And Anoter One \n1ne more time\n")

print("""The big one text
on multiple lines\n:
it ends.
but only after last one
line
""")

tabbed="\tTabbed text"
slashes="text\\ has \\ mul\\tip\\le\\\\slashes"
list="""
fat text with list:
\t* one
\t* two
\t* three\t or\t some/thing"""
print(tabbed, slashes, list)

#multiline comment in notepad plus plus
#In the position where you want to add text, do:
#Shift + Alt + down arrow

#Escape What it does.
#\\ Backslash (\)
#\' Single-quote (')
#\" Double-quote (")
#\a ASCII bell (BEL)
#\b ASCII backspace (BS)
#\f ASCII formfeed (FF)
#\n ASCII linefeed (LF)
#\N{name} Character named name in the Unicode database (Unicode only)
#\r Carriage return (CR)
#\t Horizontal tab (TAB)
#\uxxxx Character with 16-bit hex value xxxx
#\Uxxxxxxxx Character with 32-bit hex value xxxxxxxx
#\v ASCII vertical tab (VT)
#\000 Character with octal value 000
#\xhh Character with hex value hh
