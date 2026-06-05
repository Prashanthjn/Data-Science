class Student:

    school="aiet"

    def __init__(self,name,age,usn):
        self.name=name
        self.usn=usn
        self.age=age

    def Show(self):
        print(f'name:{self.name}\nusn:{self.usn}\nage:{self.age}')


    @classmethod
    def hii(cls):
        print('hello \n',cls.school)
       
    
    @staticmethod
    def Stat():
        print("static method")
        




s1=Student('prashi',20,'cd032')
s1.Show()
s1.Stat()
s1.hii()