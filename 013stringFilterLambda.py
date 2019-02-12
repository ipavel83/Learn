#py3.7
import string
print(string.printable)
print([c for c in string.printable])

str = "\n\t\nHE\aLLO\n\t\n\17\b"
procd = [c for c in str]
print(procd)
str = filter(lambda x: x in string.printable, str)
procd2 = [c for c in str]
print(procd2)
