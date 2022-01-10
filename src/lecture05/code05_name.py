# define a function named print_hello
def print_hello():
    print('Hello!')


# assign a name to an object
a = 2                     # a is 2's name
print(2, id(a), type(a))  # can access 2 through its name a
a = a + 1                 # a is 3's name after this line executed
print(3, id(a), type(a))  # can access 3 through its name a
b = 2                     # b is 2's name
print(2, id(b), type(b))  # can access 2 through its name b
c = 2                     # c is 2's another name
print(2, id(c), type(c))  # can access 2 through its name c
a = 'Hello World!'        # a is the name of string 'Hello World!'
print('Hello World!', id(a), type(a))
a = [1, 2, 3]             # a is the name of list [1, 2, 3]
print('[1, 2, 3]', id(a), type(a))
a = print_hello           # a is the name of function print_hello
print('print_hello', id(a), type(a))
a()                       # it can be called



