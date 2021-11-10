# function-function return
def twice(f):
    def result(x):
        return f(f(x))    # note the scope of f()
    return result

plus_three = lambda i: i + 3

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
def e(i):
    return i + 3
x = twice(e)(7)    # note the syntax: twice() takes e(), returning a function, which is then passed 7
print(x)

