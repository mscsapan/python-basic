letters = ('A','B','c','d','E','F','g','H')

new_letters = ['H','i','J','k','L','M','N']

# print(type(letters))

convert_letters = list(letters)

convert_letters.append(len(letters))

convert_letters.extend(new_letters)


letters = tuple(convert_letters)


# multiply_tuple = letters * 2


# for i in range(len(letters)):
#     print(letters[i])

print(letters.count('H')) # return how much H is present to this tuple
print(letters.index('H')) # return first occurence position of H inside this tuple
# print(multiply_tuple)

# for i in dir(letters):   
#     print(i)

# pack - unpack tuple
# fruits_name = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango") #pack tuple

# (*fruits1,fruits2,fruits3) = fruits_name #unpack tuple
# print(fruits1)
# print(fruits2)
# print(fruits3)
