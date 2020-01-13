def parseString (expression):

    print(expression)##########

    openPar = ['('] 
    closePar = [')'] 
    queue = [] 
    result = []
  
    def doSomethingUseful(string):
        result.append(string)
        
  
    for pos, char in enumerate(expression): 
        #print(pos, char)
        if char in openPar: 
            queue.append([pos, char]) 
        elif char in closePar: 
            if len(queue) == 0: #or i != queue.pop():
                #print('error', expression, result, queue, pos, char)
                return "no open parentneses for {i}" 
            temp = queue.pop()
            #print('closePar', temp, queue)
            if len(queue) == 0:
                doSomethingUseful(parseString(expression[temp[0]+1:pos]))
        elif len(queue) == 0:
            doSomethingUseful(char)
        
    if len(queue)>0:
        #print('error at end', expression, result, queue)
        return "unBalanced"
        
    print(result)
    
    return '{' + ','.join(result) + '}'
    
    
if __name__=='__main__':
    print(parseString('1+2*(8+3+9+1-(1*2)) +()-34'))
    print('----------------')
    print(parseString('(1+2+3+4-(5*6))'))