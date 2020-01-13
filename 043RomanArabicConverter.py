#small Roman numbers converter (up to 4000)

def toRoman(arabic):
    romanDict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    result = []
    for ara, rom in romanDict.items():
        result.append( arabic // ara * rom)
        arabic %= ara
    return ''.join(result)
	
def toArabic(roman):
    romanVal = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    result = 0
    for i in range(len(roman)):
        if i > 0 and romanVal[roman[i]] > romanVal[roman[i - 1]]:
            result += romanVal[roman[i]] - 2 * romanVal[roman[i - 1]]
        else:
            result += romanVal[roman[i]]
    return result
    
    
def convertAndPrint(number):
    print(f'number: {number}', toRoman(number), toArabic(toRoman(number)))

    

convertAndPrint(1)
convertAndPrint(3)
convertAndPrint(4)
convertAndPrint(5)
convertAndPrint(9)
convertAndPrint(10)
convertAndPrint(11)
convertAndPrint(18)
convertAndPrint(25)
convertAndPrint(42)
convertAndPrint(53)
convertAndPrint(72)
convertAndPrint(87)
convertAndPrint(99)
convertAndPrint(100)
convertAndPrint(101)
convertAndPrint(151)
convertAndPrint(171)
convertAndPrint(199)
convertAndPrint(804)
convertAndPrint(1999)
#input()