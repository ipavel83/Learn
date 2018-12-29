#py3.7
from sys import argv

script, filename = argv[0], argv[1]
print(f"args: {argv}")

txt = open(filename)
print(f'file named "{filename}" contents:')
print(txt.read())

print(f'file named "{filename}" contents by line by line in list:')
txt = open(filename)
print(txt.readlines())

print("type the filename to read again:")
anotherFile = input("> ")
print(open(anotherFile).read())