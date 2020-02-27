#https://docs.python.org/3/library/pathlib.html
from pathlib import Path

print(__file__)
#1 [Python-Dev] __file__ is not always an absolute path
#https://mail.python.org/pipermail/python-dev/2010-February/097461.html

#2 Module __file__ attributes (and related values) should now always contain absolute paths by default,
# with the sole exception of __main__.__file__ when a script has been
# executed directly using a relative path. 
#(Contributed by Brett Cannon in https://bugs.python.org/issue18416)


cwd = Path.cwd()
print('0', cwd)
print('1', Path(__file__))

p = Path(__file__).resolve()
#Path.resolve(strict=False)
#Make the path absolute, resolving any symlinks. A new path object is returned

print('2', p, type(p))
print(p, str(p)) #getting string from Path object
print(p, 'exists:', p.exists(), ', is_directory:', p.is_dir())
print(p, 'is_file:', p.is_file())
print()

p_parent = Path(__file__).resolve().parent ##script dir
print('3', p_parent, type(p_parent)) ##script dir
print(p_parent, 'exists:', p_parent.exists(), ', is_directory:', p_parent.is_dir())
print(p_parent, 'is_file:', p_parent.is_file())
print()

nep = non_existent_path = Path('sooome path that should not.be/existed')
print(non_existent_path)
print(nep, 'exists:', nep.exists(), ', is_directory:', nep.is_dir())
print(nep, 'is_file:', nep.is_file())
print()

p_anchor = p.anchor
print('4', p_anchor, type(p_anchor))
p_name = p.name
print('5', p_name, type(p_name))
p_stem = p.stem
print('6', p_stem, type(p_stem))
p_suffix = p.suffix
print('7', p_suffix, type(p_suffix))
p_drive = p.drive
print('8', p_drive, type(p_drive))

p_parent_parent = Path(__file__).resolve().parent.parent
print('parent', p_parent_parent)
print()

#p.open(mode='r', buffering=-1, encoding=None, errors=None, newline=None)
#Open the file pointed to by the path, like the built-in open() function does:

with open(p, 'r') as f:
    print('opened using standart open')
    print('script file contents:')
    print(f.read())
    print()

with p.open("r") as f:
    print('opened using Path.open')
    print('script file contents:')
    print(f.read())
    print()
    
license = p_parent.joinpath('LICENSE')
print('license', license, type(license))
license = p_parent / 'LICENSE' ###good way
print('license', license, type(license))
print()

try:
    with license.open("r") as f:
        print(license, 'file contents:')
        print(f.read())
except:
    print(license, "can't, be read")


input('>>Thats end of script, input anything to exit')