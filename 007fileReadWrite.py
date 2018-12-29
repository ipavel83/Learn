#py3.7
from sys import argv

script, filename = argv[0:2]


print(f"if you want to erase {filename} type: yes")
question = str(input('>'))
#print(question, question.upper(), question.capitalize(), question.upper(), question.upper() == "YES")
if question.upper() == "YES":
	print('You choose to erase file')
	try:
		
		txt = open(filename)
		try:
			print(f"file {filename} contents: {txt.read()}")
			print("and at position 4 folows 8 chars")
			txt.seek(4)
			print(txt.read(8))
			print()
		finally:
			txt.close()
		
		try:
			txt = open(filename, 'w')
			print('Truncating file')
			txt.truncate()
			print('now input 3 strings')
			def input_and_writen(file, prompt):
				file.write(input(prompt))
				file.write('\n')
			input_and_writen(txt, '1 string> ')
			input_and_writen(txt, '2 string> ')
			input_and_writen(txt, '3 string> ')
		finally:
			print('closing file')
			txt.close()
	except IOError:
		print(f"can't open file {filename}")

	#target = open(filename
