def function1(varA,VarB):
    message='hi everyone'
    print(varA)
    def inner_function(varA,varB):
        print(f'inner_function local scope: {locals()}')
    inner_function(444,1635)

function1(5,22)

#
def function1(varA,VarB):
    message='hi everyone'
    print(varA)
    def inner_function(varA,varB):
        print(f'inner_function local scope: {locals()}')
    inner_function(444,44)

function1(44,22)

#
print((lambda x: x+4)(5))
print((lambda x: x*4)(5))
print((lambda x: x/2)(20))
print((lambda x: x/3)(20))


myList=[5,3,8,1,98,55,33,44]
print(sorted(myList))

