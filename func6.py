def squareN(num):
    if num ==0:
        return 'It is undefined'

    if num >0:
        return num**2
    
    if num <0:
        return (-1*num)**2 
    
print(squareN(5))
print(squareN(-5))
print(squareN(-12))
print(squareN(0))