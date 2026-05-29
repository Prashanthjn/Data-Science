from abc import ABC, abstractmethod

class abstract(ABC):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Square(abstract):

    def __init__(self,side):
        self.side=side


    def area(self):
        return(self.side * self.side)

    def perimeter(self):
        return(self.side * 4)

class Circle(abstract):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return(2*3.14*self.radius)

obj=Circle(4)
print(f'circle are: {obj.area()}')
print(f'circle perimeter:{obj.perimeter()}')

obj2=Square(4)
print(f'square are:{obj2.area()}')
print(f'square permeter:{obj.perimeter()}')