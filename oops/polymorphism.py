class Teacher:
    def speak(self):
        print('teacher teaches')
class Singer(Teacher):
    def speak(self):
        print('singer sings')
class Student(Singer):
    def speak(self):
        print('student answers')

s=Student()
s.speak()




class Animal:
    def show(self):
        print('show animal')
class Human:
    def show(self):
        print('show human')

a=Animal()
h=Human()

a.show()
h.show()