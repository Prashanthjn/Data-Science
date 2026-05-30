#used to add extra functions to existing code 
#they just change the existing functions 

def comment(current_function):
    def function_inside_decorator():
        print('haiiii')
        current_function()
        print('baiiii')
    return function_inside_decorator

@comment
def hello():
    print('the start of program')

hello()


