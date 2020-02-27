#py3.7
import string
print(string.printable)
print([c for c in string.printable])

s1 = "\n\t\nHE\aLLO\n\t\n\17\b"
print('s1', s1)
procd1 = [c for c in s1]
print(procd1)
s2 = ''.join(list(filter(lambda x: x in string.printable, s1)))
print('s2', s2)
procd2 = [c for c in s2]
print(procd2)
