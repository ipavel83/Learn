#py3.7
#https://docs.python.org/3.8/library/time.html

import time

t = time.time()
print(t)
print(time.gmtime(t))
print(time.localtime(t))
read = input()
t2 = time.time()
print(t2)
print(f'{t2-t}')
print(f'{t2-t:.2f}')
