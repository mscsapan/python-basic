# number = 'Ali' ' '* 8

# print(type(number))

# def numers(**kwargs):
#     return kwargs

# result = numers(name='Ali',age=26,address='Dhaka, Bangladesh')

# for key, value in result.items():
#     print(f'{key} - {value}')


my_list = ['a','b','c','d','e','f','g']

my_tuple = tuple(my_list)


# for key, value in enumerate(my_list):
#     print(f'{key} - {value} - {type(value)}')

# for key, value in enumerate(my_tuple):
#     print(f'{key} - {value} - {type(value)}')

a, b, c , *d= my_tuple

print(type(d))