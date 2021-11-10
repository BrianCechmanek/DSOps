''' Simplest of Decorators. '''

def cowsay():
    print("""
    _______________________ 
    < Hello, bovine world!  >
    ----------------------- 
            \   ^__^
            \   (oo)\_______
                (__)\       )\\/\\
                    ||----w |
                    ||     ||
    .....I..I.II..I....I.II.I...."""
    )


def my_decorator(func):
    def wrapper():
        # add in some extra behaviour
        print("print before function call")
        # call the passed function, do not modify it
        func()
        # add in some other extra behaviour
        print("print after function call")
    return wrapper


# call my_decorator, with the cowsaw arg 
my_func = my_decorator(cowsay)
print(f"what is my func: {my_func}")

# my_func is now just a function, which we can call
my_func()