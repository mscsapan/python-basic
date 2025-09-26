# 1.single level inheritance
# 2.multi level inheritance
# 3.multiple inheritance

class Car:
    def __init__(self,name, color):
        self.name = name
        self.color = color
        
    @staticmethod
    def start():
        print('Car is starting now...')
        
    @staticmethod
    def stop():
        print('Car stoped...')
        

class Brand:
    def __init__(self, brand_name, type):
        self.brand_name = brand_name
        self.type = type
        



class Lamborgini(Car, Brand):
    def __init__(self, name, color,brand_name, type):
        Car.__init__(self,name, color)
        Brand.__init__(self,brand_name,type)
        


lam = Lamborgini('Aventador', 'red','Lamborgini','Fuel')

print(lam.brand_name)