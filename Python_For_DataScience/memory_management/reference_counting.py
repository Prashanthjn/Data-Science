a=[1,2,3,4,5]
b=a

print(a)
print(id(a),id(b))     #both have same id means both are referring same location if one changes it'll reflect in other too
b.append(6)
print(a)