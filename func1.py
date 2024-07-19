'''def performOperation(args):
    print(args)

print(performOperation(1,2,3))
          ^^^^^^^^^^^^^^^^^^^^^^^
TypeError: performOperation() takes 1 positional argument but 3 were given'''


def performOperation(*args): # when you put * before args the problem gets solved
    print(args)

performOperation(1,2,3) # we did not use print and got them on terminal

##
def multiSum(num1,num2):
    return num1+num2

print(multiSum(5,4)) ## you have to print it to see the result on terminal


