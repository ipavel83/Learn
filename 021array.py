#py3.7

tuple1 = ('one', 'andTwo', 3, 'four')
#del tuple1[1] #TypeError: 'tuple' object does not support item deletion
print(tuple1)

list1 = [el for el in tuple1]
list2 = list(tuple1)
print(list1)
print(list2)
del list2[1]
print(list2)

print(tuple1)

numtuple1 =(1.0, 0.7, 1.5, 220, 2.5)
#############Array mutable
import array
arr1 = array.array('f', numtuple1) #220 converted to float
print(arr1) #0.7 converted to float also
arr1[2] = 0.2
print(arr1)

arr2 = array.array('d', numtuple1) #220 converted to double
print(arr2) 
arr2[2] = 0.2
print(arr2)
print(numtuple1)

from sys import getsizeof
numtuple2 = (0, 1, 2, 3, 5, 9, 15, 255)
############# immutable bytes
bArr1 = bytes(numtuple2)
bArr2 = b'\x00\x01\x02\x05\x09\x15\xff'
bArr3 = b'x00x01x02x05x09x15xff' #without backslashes it just [x,0,0,x,0, ...etc]
print(bArr1, bArr1[2]) #ok 2
print(bArr2, bArr2[2]) #ok 2
print(bArr3, bArr3[2]) #48 is Ascii code of symbol 0 (zero) 
print('size of bytes:', getsizeof(bArr1), getsizeof(bArr2), getsizeof(bArr3))
print(b'0123'[0],b'0123'[1],b'0123'[2],b'0123'[3])
