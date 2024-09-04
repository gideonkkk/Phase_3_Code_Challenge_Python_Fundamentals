def decorator_func(original_func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return original_func(*args, **kwargs)
    return wrapper
def apply_decorator(func):
    decorated_func = decorator_func(func)
    return decorated_func
def my_function():
    print("Original Function Called")
decorated_my_function = apply_decorator(my_function)
decorated_my_function()