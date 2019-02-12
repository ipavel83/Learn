#!/usr/bin/env python3
#py3.7

with open('hello_foo.txt', 'w') as f:
    f.write('hello, world!')
#same as:
# f = opent('hello_foo.txt', 'w')
# try:
#     f.wtite('hello, world')
# finally:
#     f.close()
    
with open('hello_foo.txt', 'r') as f:
    print(f.read())
    
print()

    
#more advanced:
    
from contextlib import contextmanager
import os

@contextmanager # https://stackoverflow.com/a/3012921
def working_directory(path):
    current_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    except:
        print(f"directory {path} not found")
    finally:
        os.chdir(current_dir)
        
#Pavel: enclosed with block to get rid of error if directory is not found
    #should think later if possible to handle such things inside "with" block
try:
    with working_directory("data/stuff"):
        # do something within data/stuff
        print('Hi')
except:
    print('problem with with of directory data/stuff')
finally:
    print('first try final')
# here I am back again in the original working directory

print()

#Another way: https://stackoverflow.com/a/5205878/5233335
try:
    f = open('foo.txt')
except IOError:
    print('error open "foo.txt"')
else:
    with f:
        print('foo opened')
        print(f.readlines())
        #
        # some_code
        #

