class Animal:
    
    def __init__(self,name,age):
        self.name = name,
        self.age = age,
        print(f'name: {self.name}, age : {self.age}')
        
    
    # def __str__(self):
    #      print(f'name: {self.name}, age : {self.age}')
    
    def animal_name(self):
        return 'Hello function'
        


animal = Animal('Ali',26)

# name = animal.animal_name()
# print(animal.animal_name())

animal.name