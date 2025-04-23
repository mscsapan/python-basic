# find out the smallest and largest number from the list

mylist = [-10,-2,-5,-3,-6]

# long approach
# smallest = largest = mylist[0]

# for i in mylist:
#     if smallest > i:
#         smallest = i
    
#     if largest < i:
#         largest = i

# short approach
smallest = min(mylist)
largest = max(mylist)
        
print(f'Smallest number is {smallest} - Largest number is {largest}')
