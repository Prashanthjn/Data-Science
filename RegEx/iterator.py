class Odd:
    def __iter__(self):
        self.v=1
        return self
    
    def __next__(self):
        x=self.v
        self.v+=2
        return x
       
odd=Odd()
it=iter(odd)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))