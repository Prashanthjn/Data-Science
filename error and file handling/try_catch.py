try:
    n=10
    m=30
    res=n/m
except ZeroDivisionError:
    print("division by zero !")
else:
    print("result is ",res)
finally:
    print('executed ')