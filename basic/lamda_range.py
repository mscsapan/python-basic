# mylist = {'name': 'John', 'age': 25.9, 'city': 'New York', 'country': 'USA'}

# number = range(1,11)

# my_list = list(filter(lambda x: x % 2 == 0 ,number))


# # print(*mylist.values()), 
# print(f'Numbers : ', *number),
# print(f'List : {my_list}'),

def myfunc(n):
  return lambda a : a * n if a > 0 else n

mytripler = myfunc(3)

print(mytripler(0))