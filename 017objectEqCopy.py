#!/usr/bin/var python3
#py3.7

a = [1,2,3,]
b = a
c = [1,2,3,]
print(a == c, a is b)
print(a == c, a is c)
print(None == None, None is None)

import copy
d =[a,b,c,3]
copyE = copy.copy(d)
deepF = copy.deepcopy(d)
print(d)
print(copyE)
print(deepF)
print('change d[0][1]=7')
d[0][1]=7
print(d)
print(copyE)
print(deepF)
print('change d[1]=8, deepF[2][1]="deep"')
d[1]=8
deepF[2][1]= 'deep'
print(d)
print(copyE)
print(deepF)