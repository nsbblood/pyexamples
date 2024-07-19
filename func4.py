def performOperation(num1,num2,operation='sum'):
    print(locals())

performOperation(1,3, operation='sum')
performOperation(1,3, operation='muliply')

print(globals())