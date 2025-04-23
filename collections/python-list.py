mylist = [-10,-2,-5,-3,-6]


# Get Smallest Number in List

smallest = largest = mylist[0]

for i in mylist:
    if smallest > i:
        smallest = i
    
    if largest < i:
        largest = i
        
print(f'Smallest number is {smallest} - Largest number is {largest}')
