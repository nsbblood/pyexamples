myList=[1,2,3,4,5,6,7]

for item in myList:
    print(item)

myList=['Istanbul','Hamburg','Hannover','Bremen','Düsseldorf','Malatya','Berlin']

for cities in myList:
    print(cities)

newCities=myList.copy()
newCities.append('Mannheim')
print(newCities)

newCities.remove('Istanbul')
print(newCities)

