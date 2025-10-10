# mylist = {'name': 'John', 'age': 25.9, 'city': 'New York', 'country': 'USA'}

# def my_function(name):
#     return name

# name = my_function(mylist)

# print(type(name))


# normal function

# def normal_func():
#     print('hello world')
    

# positional function arguments function

# def parameter_func(x):
#     return x

# result = parameter_func('Ali') #or parameter_func(x ='Ali')


# positional function arguments function

# def key_val_func(*,x):
#     return x

# result = key_val_func(y = 3)


def key_val_func(a, b, /, *, c, d):
    return (a+b) - (c+d)


result = key_val_func(10,4,c = 4, d = 5)
print(result)