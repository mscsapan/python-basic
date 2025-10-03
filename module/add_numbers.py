def add_numbers(*args):
    result = 0
    for i in args:
        if not isinstance(i,str):
            result += i
    return result