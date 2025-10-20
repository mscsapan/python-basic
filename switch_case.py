
'''
day = 10

match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
  case _: #this is default case
    print('Not in day range')

'''


month = 4
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4: # | is called as pipe operator
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")