z=10
y=10

print(id(z),id(y))   # here python doent create new object for z and y cz they have same value in it

z+=1
print(id(z),id(y))   # now the id has been changes sisce it has diffrent value