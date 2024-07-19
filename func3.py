import math

def perfOperation(*args, operation='sum'):
    if operation=='sum':
        return sum(args)
    if operation=='multiply':
        return math.prod(args)
    
print(perfOperation(5,8, operation='multiply')) 
#normally I did not need to use print but in if I did not use print!! take care!!

print(perfOperation(5,8, operation='sum')) 

# print(perfOperation(5,8, 'multiply')) 
#TypeError: unsupported operand type(s) for +: 'int' and 'str'


