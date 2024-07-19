def performOperation(*args,**kwargs):
    print(args) #when you print them dont use * !
    print(kwargs)

performOperation(1,2,3, operation='sum')

#

def hList(*args,**kwargs):
    print(args)
    print(kwargs)

hList(1,2,3,4,5, name='eli', name2='ns')

#
def hLists(*args,**kwargs):
    print(args)
    print(kwargs)

hLists(1,2,3,4,5, city='hamburg', city2='berlin', city3='hannover', city4='bremen')

# Under one performOperation we could do all of these!


'''def performOperation(*args,**kwargs):
    print(args) #when you print them dont use * !
    print(kwargs)

performOperation(1,2,3, operation='sum')
performOperation(1,2,3,4,5, name='eli', name2='ns')
performOperation(1,2,3,4,5, city='hamburg', city2='berlin', city3='hannover', city4='bremen')
'''