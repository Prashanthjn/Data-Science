def vote(age):
    if age<18 and age>0:
        raise Exception("cannot vote")
    print(f"age is {age}")
try:
    vote(-67)
except ValueError as e:
    print(e)