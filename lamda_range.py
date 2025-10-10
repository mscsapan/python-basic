mylist = {'name': 'John', 'age': 25.9, 'city': 'New York', 'country': 'USA'}

number = range(1,11)

# for i in number:
is_numeric = filter(lambda x : type(x) == str, mylist.values()) 

# print(*mylist.values()),
print(is_numeric),