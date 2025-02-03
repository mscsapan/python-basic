# 01. Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

# def count_chars(name):
#     dict = {}
#     keys = dict.keys()
#     for i in name:
#         if i in keys:
#             dict[i] += 1
#         else:
#             dict[i] = 1
#     return dict

# print(count_chars('https://www.google.com'))
    
    
# 02. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'


def first_last_chars(name):
    if len(name) < 2:
        return ''
    else:
        return name[:2] + name[-2:]

print(first_last_chars('w3resourcew'))