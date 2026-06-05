class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def __str__(self):                                                              #this is called dunder method & automatically get called when you perform certain actions on an object
        return f'hello {self.name}'                                           
    
    def __add__(self, other):
        sum=0
        for i in other:
            sum+=i.age
        return f'sum of age {self.age + sum}'

obj=Animal('prashi',20)
obj2=Animal('dolphin',20)
obj3=Animal('tiger',20)
print(obj+(obj2,obj3))
print(obj)