list_numbers = [1,2,3,4,5,6,7,8,9]
tuple_numbers = (1,2,3,4,5,5,5,6,7,8,9,10)
dict_numbers = {'name':'Ali','age':26}
set_numbers = {1, 2, 3, 4, 5, 6, 7}

print(tuple_numbers.count(5))
num = [*list_numbers,tuple_numbers]

print(num)
print(len(num))
# for i in dir(set_numbers):
#     print(i)
