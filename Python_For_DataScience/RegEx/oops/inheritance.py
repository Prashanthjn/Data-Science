#single level inheritance
class Animals:
    head="this is the animal class"

    def __init__(self,name,color):
        self.name=name
        self.color=color
    def show(self):
        print(f'name:{self.name}\ncolor:{self.color}')

class Dog(Animals):
    def __init__(self,name,color,age):
        super().__init__(name,color)
        self.age=age

    def show(self):
        print(f'name:{self.name}\ncolor:{self.color}')
        print(f'age:{self.age}')


b=Dog('tommy','white',2)
c=Animals('puttu','orange')
b.show()
c.show()
print('-----------------------------------------------------------------------------------------------------------------------')

#------------------------------------------------------------------------------------------------------------------------------------------

#multiple inheritance

class Sheep:
    name1='sheep'
    def __init__(self,name):
        self.name=name


class Cow:
    name2='cow'
    age=21
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age


class Buffalo(Cow,Sheep):          #here the Cow will be seen first that is method resolution  order 
    def __init__(self, name,age,color):
        super().__init__(name,age)
        self.color=color

d2=Buffalo('lord',23,'blue')
print(d2.name1)
print(d2.name)
print(d2.name2)
print(d2.age)
print('-----------------------------------------------------------------------------------------------------------------------')

#------------------------------------------------------------------------------------------------------------------------------------------

#multilevel inheritance
class Factory:

    def __init__(self,material,zips):
        self.material=material
        self.zips=zips
    
class Bhopal_Factory(Factory):
    def __init__(self,material,zips,color):
        super().__init__(material,zips)
        self.color=color

class Pune_Factory(Bhopal_Factory):
    def __init__(self, material, zips, color,pocket):
        super().__init__(material, zips, color)
        self.pocket=pocket



d = Pune_Factory('nylon', 3, 'blue', 4)

print(d.material)
print(d.color)