# Decorators: Why you see them, Why you want them 

Definition: a [higher-order function](https://en.wikipedia.org/wiki/Higher-order_function) which takes another function as an argument and extends the behaviour of this argument function, without otherwise modifying it. 


**Key Concepts**

* Functions can return functions
* funcftions can accept functions as arguments

# Common Encounters

* Flask/Fast API
* numba/jit
* Python: `@classmethod`, `@staticmethod`, `@property`, `@dataclass`
* `@functools.wrap`, `@debug` -> https://realpython.com/primer-on-python-decorators/
* \<ADD MORE\>
* chaining decorators (sure, why not)

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



# Decorator method signatures

* what happens when you want to debug, or there is an argument error? 