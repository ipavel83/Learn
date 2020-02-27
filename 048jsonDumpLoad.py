#run in local path!
import sys    
import os    
import json

file_name =  os.path.basename(sys.argv[0])
print(file_name)
file_name = os.path.splitext(file_name)[0]
print(file_name)
json_file_name = file_name + '_data.json'
print(json_file_name)

a = {'name': 'John Doe', 'age': 24}
print(a)

try:
    with open (json_file_name, 'r') as initialFile:
        print('file already exist:')
        already = json.load(initialFile)
        print( already)
        print('will add +1 to loaded age')
        a['age'] = already['age']+1
except FileNotFoundError as e:
    print('file initially not exist, its fine', e, e.errno)

js = json.dumps(a, sort_keys=True, indent=4, separators=(',', ': '))
print(js)
with open(json_file_name, 'w+') as fw:
    fw.write(js)
    
with open(json_file_name, 'r') as fr:
    b = json.load(fr)
    
print( b, b['name'], b['age'], type(b['age']) )