class Animal:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(f'name: {self.name}, age : {self.age}')
        
    
    # def __str__(self):
    #      print(f'name: {self.name}, age : {self.age}')
    
    def animal_name(self):
        return 'Hello function '+self.name
        


animal = Animal('Ali',27)

print(animal.animal_name())


# name = animal.animal_name()