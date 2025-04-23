# multiply each item from a list

mylist = [1, 0,2, 3]

result = 1

for i in range(len(mylist)):
    # if mylist[i] != 0:
    if mylist[i] > 0:
        result *= mylist[i]
        # print(f'number {result} * {mylist[i]} = {result}')

print(f'Multiply each elements is {result}')