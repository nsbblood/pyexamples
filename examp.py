class Dog:

    def __init__(self,name):
        self.name=name
        self.legs=4

    def speak(self):
        print(self.name+ ' says: Bark! Bark! ')

    def looking(self,direction):
        print(self.name + ' looking at {direction}') #??

    

Dog('Hugo').speak() # dont forget to put () when you call a func from a class

Dog('Cute Dogie').speak()

Dog('Lia').looking(direction='to me')