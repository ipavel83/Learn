import csv

outFileName = __file__+'_out.csv'

outFile = open(outFileName, 'w', newline='')
outWriter = csv.writer(outFile)
outWriter.writerow(['a', 'b', 'cccc', 'dee', 'e', '2f', '3'])
outWriter.writerow(['say something:', 'who?', 'You!', 'hello!'])
outWriter.writerow([1,2,3,4.4, 5])
outFile.close()

with open(outFileName, 'r') as rf:
    print(rf.read())


with open(outFileName, 'r') as rf:
    outReader = csv.reader(rf)
    outData = list(outReader)

print(outData)
print()

print('now print by row:')
for row in outData:
    print(row)