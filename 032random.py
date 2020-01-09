#py3.7

#random(), uniform(startFloatIncl, endFloatIncl), randint(startIntIncl, endIntIncl)
# and much much more (like seed(), intervals or population choise) in https://docs.python.org/3/library/random.html
from random import random, uniform, randint 


print('just random',random())
print('random floating point number in interval', uniform(5.5, 25.8))
print('random int in interval', randint(10,100))