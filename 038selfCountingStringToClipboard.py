#py3.7
#pip install pyperclip
print('Program will make self counting string and copy it to clipboard')

try:
    import pyperclip
except ImportError:
    pyperclip = None
    print("pyperclip module not found, result won't be copyed to clipboard")

filler = '*'
print('Filler between numbers is - ', filler)
howLong = int(input('Input length of desirable self counting string >>> '))

result = ''
remainder = howLong
while remainder >= (len(str(remainder))):
    result = str(remainder) + result
    remainder -= len(str(remainder))
    #print(result, remainder)
    if remainder >= len(filler):
        result = filler +result
        remainder -= len(filler)
        #print(result, remainder)
        
print('Result is:', result, ',it length is:', len(result))
if pyperclip:
    pyperclip.copy(result)
    input('Result was copied to clipboard, press ENTER to exit')