class Factory:
    a="pune"                        #public
    _b="not pune"                   #protected this convention has nothing to do with but just used to show to the developer that this is protected variable
    __c=120000                      #private cannot be accessed from anywhere outside the class

    def _show(self):                      #protected can be used for methods too
        print("hi from pune factory")
       # print(self.__c)
        print(Factory.__c)          # way to acccess the private variable from outside the class 

class Bhopal(Factory):
    def show2(self):
        print(super().a)
        print(super()._b)
       # print(super().__c)          #tried accessing the private variable 
        
obj=Bhopal()
obj._show()
obj.show2()