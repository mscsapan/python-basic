def universal_decorator(func):
    def wrapper(*args, **kwargs):
        print("---- Function start ----")
        print(f"Calling: {func.__name__}")
        print("Positional args:", args)
        print("Key word args:", kwargs)
        
        result = func(*args, **kwargs)   # actual function
        print("result:", result)
        print("---- Function end ----\n")
        return result
    return wrapper


# without passing any arguments
@universal_decorator
def say_hello():
    return "Hello Python!"


# passing positional arguments
@universal_decorator
def add_numbers(a, b, c):
    return a + b + c


# passing keyword arguments
@universal_decorator
def greet(name, city="Dhaka"):
    return f"{name} live in {city}"



# passing both args & kwargs arguments
@universal_decorator
def introduce(name, *hobbies, **details):
    msg = f"I\'m {name}. My hobbies: {', '.join(hobbies)}।"
    for key, value in details.items():
        msg += f" {key} is {value}."
    return msg


say_hello()

add_numbers(10, 20, 30)

greet(name="Ali", city="Rajshahi")

introduce("Mohammad", "reading", "gaming", "coding", age=22, profession="student")