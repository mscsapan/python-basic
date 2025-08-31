
'''
True or 1 | False or 0 are same elements and trated as duplicate for set collection
'''
fruits_name = {"apple", "banana", "cherry", "apple",True,1}

# extendable_list = {"orange","melon", "mango"}
extendable_list = {"orange",3,90.2}

fruits_name.add('pineapple')

fruits_name.update(extendable_list)

# fruits_name.remove(1) # fruits_name.remove(True)

# fruits_name.remove('orangee') # if item is not a member of a set then raise an exception

# fruits_name.discard('orange') # if item is not a member of a set then does not raise an exception

# print(f'before {fruits_name}')

# fruits_name.pop() # removed an item from a set randomly, you can not specefied item


# for i in fruits_name:
#     print(f'type {type(i)} - {i}')

# print(f'after {fruits_name}')

for i in dir(fruits_name):
    print(i)
    

