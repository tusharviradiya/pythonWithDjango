# decorators in python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start} seconds")
        return result
    return wrapper

def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join([str(arg) for arg in args])
        kwargs_value = ', '.join([f"{key}={value}" for key, value in kwargs.items()])
        print(f"{func.__name__}({args_value}, {kwargs_value})")
        return func(*args, **kwargs)

    return wrapper

@debug
def greet(name, greeting="hello"):
    print(f"{greeting} {name}")

@debug
def hello():
    print("hello")

# @timer
# def example_function(n):
#     time.sleep(n)

# example_function(2)
hello()
greet("tushar", "hi")