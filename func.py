def performOperation(num1,num2,operation, message='Hi there'):
    print(message)
    if operation=='sum':    # ==  ' '
        return num1+num2
    if operation== 'multiply':
        return num1*num2
    
print(performOperation(5,4,'sum'))  # you need to use 'operator' -> 'sum' or 'multiply'

result=performOperation(3,12,'multiply')
print(result)

print(performOperation(33,11,'sum',message='Lets go to Hamburg ?'))
