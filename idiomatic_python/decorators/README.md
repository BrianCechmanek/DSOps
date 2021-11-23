# Decorators: Why you see them, Why you want them 

Definition: a [higher-order function](https://en.wikipedia.org/wiki/Higher-order_function) which takes another function as an argument and extends the behaviour of this argument function, without otherwise modifying it. 


**Key Concepts**

* Functions can return functions
* funcftions can accept functions as arguments

# Common Encounters

* Flask/Fast API: `@app.route('/')`
* numba/jit: `@jit(nopython=True)`
* Pure Python: `@classmethod`, `@staticmethod`, `@property`, `@dataclass`
* `@functools.cache`: https://docs.python.org/3/library/functools.html
* chaining decorators (sure, why not)

# Motivations

A: Any time you wish to augment a function, without effecting it's underlying behaviour. 

Take the archetypal example of figuring out how long a function takes to run:

```python
def my_func():
    # mock some computation
    delay = random.randint()
    time.sleep(delay)
    # return the answer
    return 42
```

The beginner pythonista will usually write up a timer function of some type, and print out the result:

```python
def my_func():
    # add in time start
    t_0 = time.process_time()

    # do the thing
    delay = random.randint()
    time.sleep(delay)

    # and time end
    runtime = time.process_time-t_0
    print(f"process runtime was: {runtime}")

    return 42
```

This works, at a naiive level. Sure. But it will now litter up your `sys.out`, and what will you do if you have 3 different methods that you want to time. copy and paste those three lines into each function? (We've all done it)

But what we _really_ want is a `timer()` function, that we can use over and over...

```python
my_func_1(timer())    #<-can we just throw timer() at it?
my_func_2(timer())
my_func_3(timer())
```

# Break to the Demos

1. `one_higher_order.py`
2. `two_decorator_usage.py`

-----
-----
-----

# Decorator Usage

in the higher-order example: 

```
def twice(f):
    def result(x):
        return f(f(x))
    return result

@twice
def g(i):
    return i + 3
```

Care needs to be taken that **all** calls to `g()` will now invoke it `@twice`. This may be desired. or may not. Do you want to permanently change a method (see: flask/fast API).

-----
-----
-----

# TODO: Decorator method signatures

* what happens when you want to debug, or there is an argument error? 