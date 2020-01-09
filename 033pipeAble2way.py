#py3.7
#more complex variants at:
#https://stackoverflow.com/questions/34459274/how-to-make-python-scripts-pipe-able-both-in-bash-and-within-python

import sys



def processing(data)
    #do some stuff
    return data
    
    
if __name__ == '__main__':
    def multipipe(data):
        #if __main__ call processing and print result
        print(processing(data))
        
    def parse_args(input):
        #Do some sturr with input
        #like get all elements except script name:
        data = imput[1:]
        #...
        return data
        
    input = parse_args(sys.argv)
    main(input)
else:
    def miltipipe(data):
        #if called as function from other file - do processing and return result
        return processing(data)