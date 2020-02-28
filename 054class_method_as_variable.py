class NumAdd():
    def __init__(self, num):
        self.num = num
        
    def add(self, num2):
        self.num+=num2
        return self.num
        
n1 = NumAdd(2)
print(n1.num)
n2 = NumAdd(3)
#print(n1.num)
addN1 = n1.add
addN1(5)
assert n1.num == 7
print(n1.num)
input()