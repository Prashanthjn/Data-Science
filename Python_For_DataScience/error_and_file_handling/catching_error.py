try:
    n=int(12.45)
    res=1/n
except ValueError:
    print("hit with a value error")
except ZeroDivisionError:
    print("divison by zero ")
else:

    print('the result is ',res)
finally:
    print("executed the code ")