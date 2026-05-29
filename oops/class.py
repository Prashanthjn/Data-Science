class Car:
    company= "Tata"
    price= 14 

    def display(self):
        print(f"company: {self.company}")
        print(f"price : {self.price}")
print(Car.company)
print(Car.price)
Car().display()