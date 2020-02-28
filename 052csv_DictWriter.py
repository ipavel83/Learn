import csv

sample1 = {'a1': 1, 'b2': 2, 'c4': 3, 'name': 'abba'}
sample2 = {'name': 'Bob', 'b2': 'beeTwoo', 'other': 'something'}
sample3 = {'b2': 'b2', 'c4': True, 'name': 'name'}
sample4 = {}
sample5 = {'a1': None, 'b2': ''}

exampleFile = __file__+'_out.csv'

try:
    with open(exampleFile, 'r') as fr:
        odr = outDictReader = csv.DictReader(fr)
        print(f'file {exampleFile} found:')
        for i,row in enumerate(odr):
            print(f'row number: {i}', row)
            if i==0:
                sample1['a1']=int(row['a1'])+1
except:
    print(f'file {exampleFile} not found, creating new')

print()

with open(exampleFile, 'w', newline='') as fw:
	odw = outDictWriter = csv.DictWriter(fw, ['name', 'a1', 'b2', 'c4'], extrasaction ='ignore') 
        #extrasaction='ignore' used to ignore values that not in in fieldlist
	odw.writeheader()
	odw.writerow(sample1)
	odw.writerow(sample2)
	odw.writerow(sample3)
	odw.writerow(sample4)
	odw.writerow(sample5)

with open(exampleFile, 'r') as fr:
	print(fr.read())