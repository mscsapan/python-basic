person = {
    "name" : "Mohammad",
    "phone" : "01624188877",
    "email" : "mscsapan@gmail.com",
    "address" : "Dhaka, Bangladesh",
    "profession" : "Flutter developer",
    "age" : 27,
    "is_married" : True,
    "colors": ["red", "white", "blue"]
}

# for i in dir(person):
#     print(i)

# for value in person.values:
#     print(value)

# print(len(person))

# print(person['age']) # if key is not present, raise an exceptions

# print(person.get('profession')) # if key is not present, return default value e,i None

# key = person.keys()

# print(f'before {key}')

# person['nick_name'] = 'Ali'

# print(f'after {key}')

value = person.values()

# print(len(value))

for key,value in person.items():
    # print(f'{key} - {type(value)}')
    if  isinstance(value,list): # if (type(value) is list)
        for i in value:
            print(f'found - {i}')
    else:
        print(f'{key} - {value}')
