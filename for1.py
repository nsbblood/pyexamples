animalList={
    'e' : ['elaphent'],
    'd' : ['dog'],
    'c' : ['cat'],
}

for letter,animals in animalList.items(): #dont forget to add items() !
    if len(animals)==1:
       print(animals)


newAnim=animalList.copy()

newAnim['k']=['koala']
print(newAnim)


newAnim['k']='koala' #no [] 
print(newAnim)


newAnim['m']=[]  #another way to add an animal to the list
newAnim['m'].append('monkey')
print(newAnim)