# function-function return
def twice(f):
    def result(x):
        return f(f(x))  # note the scope of f()

    return result


def plus_three(i):
    return i + 3


# or as a lambda
plus_three = lambda i: i + 3

if __name__ == "__main__":
    g = twice(plus_three)
    x = g(7)
    print(x)

    # decorator syntax
    @twice
    def g(i):
        return i + 3

    x = g(7)
    print(x)

    # decorator return
    def h(i):
        return i + 3

    x = twice(h)(
        7
    )  # note the syntax: twice() takes e(), returning a function, which is then passed 7
    print(x)
