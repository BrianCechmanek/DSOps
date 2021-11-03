from typing import List, Union
from utils import benchmark, benchmark_many

# Background
# An evaluation needed to be done on three strings coming out of 
# a web scrape evaluation. Each string could be a url. 
# but specifically, the string would either be a url or nothing
a = None
b = ''
c = 'c'    # "myweb.com"
# There would always be three strings, and we never need to check
# if the url is valid or not. 


def first_str_original(a, b, c):
    # the original method that was written*
    # return first of a or b or c that is a string (not empty)
    
    if a is not None: # *More specifically, if a is not '' and a is not None:
        return a
    elif b is not None:
        return b
    elif c is not None:
        return c
    else:
        return None


def first_str_truthy(a, b, c):
    # python strings are truthy/falsy
    # a = "something" is truthy
    # a = "" is falsy
    # should we have elifs here? 
    if a:   # if None or ''
        return a
    elif b:
        return b
    elif c:
        return c
    else:
        return None


def first_str_bools(a,b,c):
    # return first of a or b or c or None
    # using boolean logic 
    return a or b or c or None


def first_str_args(*args):
    # return first of Iterable[str] using args
    return [x for x in args if x][0]


def first_str_unpacking(*args):
    # return first of args with partial unpacking
    # arguably worse than first_str_args. but more idiomatic
    # as it avoids the list slicing
    first, *rest= [x for x in args if x]
    return first


def first_str_next(*args: List[str]) -> Union[str,None]:
    # or returning from the datamodel
    return next((x for x in args if x), None)


def first_str_next_cond(*args: List[str]) -> str:
    # returning from data model
    # where calling conditional function, cond, is true
    # first_true([a,b], f) --> a if f(a) else b if f(b) else x
    def cond(x):
        return True if x else False

    return next(filter(cond, args), None)


# def use_itertools(*args):
#     # or, someone has already done it. 
#     # https://docs.python.org/3/library/itertools.html#itertools-recipes
#     from more_itertools import first_true
#    return first_true(*args, default=None)


##### Benchmarks #####
def print_benchmarks(iters=1) -> None:

    print(f"-----Benchmarks (iters={iters})-----")
    if iters==1:
        benchmark(first_str_original)(a,b,c)
        benchmark(first_str_truthy)(a,b,c)
        benchmark(first_str_bools)(a,b,c)
        benchmark(first_str_args)(a,b,c)
        benchmark(first_str_unpacking)(a,b,c)
        benchmark(first_str_next)(a,b,c)
        benchmark(first_str_next_cond)(a,b,c)
    else:
        benchmark_many(first_str_original, iters=iters)(a,b,c)
        benchmark_many(first_str_truthy, iters=iters)(a,b,c)
        benchmark_many(first_str_bools, iters=iters)(a,b,c)
        benchmark_many(first_str_args, iters=iters)(a,b,c)
        benchmark_many(first_str_unpacking, iters=iters)(a,b,c)
        benchmark_many(first_str_next, iters=iters)(a,b,c)
        benchmark_many(first_str_next_cond, iters=iters)(a,b,c)

# print("but what if we had a huge list of inputs")
# print("d=10000, first_str_next(*d, a, b, c)")
# d = [None] * 10000
# benchmark(first_str_next)(*d, a, b, c)
