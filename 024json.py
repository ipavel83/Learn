#py3.7

import json

mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee,}
print(str(mapping))
print( json.dumps(mapping, indent=4, sort_keys=True) )
#print( json.dumps({sum:'summ'}) ) #TypeError: keys must be str, int, float, bool or None, not builtin_function_or_method

#mapping['complex'] = { 1, 2, 3, } set is not serializable by dumps, but List [] is ok
#print(json.dumps(mapping)) #TypeError: Object of type set is not JSON serializable

