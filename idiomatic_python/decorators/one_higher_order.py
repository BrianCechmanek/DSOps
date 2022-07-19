""" Simplest of Decorators. """


def cowsay():
    print(
        """
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


# but we want to add some text before and after this...
def cowsaid(top_str: str = "print before", bottom_str: str = "print after"):
    print(
        f"""
    {top_str}    # added behaviour before
    _______________________ 
    < Hello, bovine world!  >
    ----------------------- 
            \   ^__^
            \   (oo)\_______
                (__)\       )\\/\\
                    ||----w |
                    ||     ||
    .....I..I.II..I....I.II.I....
    {bottom_str}"""
    )
    return 42


def higher_order(func):
    def wrapper():
        # add in some extra behaviour
        print("print before function call")
        # arbitarry work
        # call the passed function, do not modify it
        func()
        # add in some other extra behaviour
        print("print after function call")

    return wrapper


@higher_order
def briansay():
    print("hello")


# call higher_order(), with the cowsaw arg
if __name__ == "__main__":
    my_func = higher_order(cowsay)
    print(f"what is my func: {my_func}")

    # my_func is now just a function, which we can call
    my_func()
    decorated_func = higher_order(cowsay())
