#!/usr/bin/var python3
#py3.7
import traceback

class BaseValidationError(ValueError):
	pass

class NameTooShortError(BaseValidationError):
	pass
	
class NameTooLongError(BaseValidationError):
	pass
	
class Name8long(BaseValidationError):
	pass
	
def validate(name):
	if len(name) < 5:
		raise NameTooShortError(name)
	if len(name) == 8:
		raise Name8long(name)
	if len(name) >10:
		raise NameTooLongError(name)

print(traceback.format_exc()) #do no error and print "NoneType: None"

def tryValidate(name):
	print('Try to validate:',name)
	try:		
		validate(name)
	except NameTooShortError:
		print(traceback.format_exc())
		print('name too short')
	except NameTooLongError:
		print(traceback.format_exc())
		print('name too long')
	except Exception as err:
		print(traceback.format_exc())
		print(traceback.print_tb(err.__traceback__))
		print('just Exception')
	else:
		print('validation successful')
	finally:
		print('this message always prints')
		print()
		print()

tryValidate('hi')
tryValidate('aaaabbbb')
tryValidate('hello everyone!')
tryValidate('fiine')
		
	