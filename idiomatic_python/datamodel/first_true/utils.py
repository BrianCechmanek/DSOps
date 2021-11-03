from time import perf_counter, time, process_time


def benchmark(func):
    ''' Standard benchmarking decorator. '''

    def wrapper(*args, **kwargs):
        t = perf_counter()
        res = func(*args, **kwargs)
        print("Method name:", 
                f"{func.__name__ : <20}", 
            "time to execute: ", 
            f"{perf_counter()-t : >10}s")
        return res

    return wrapper


def benchmark_many(func, iters:int=333):
    ''' Benchmarking decorator for 333 runs. '''

    def wrapper(*args, **kwargs):
        t = perf_counter()
        for i in range(iters):
            res = func(*args, **kwargs)
        print("Method name:", 
                f"{func.__name__ : <20}", 
                f"time to execute {iters} times:", 
                f"{perf_counter()-t : >10}s")
        return res

    return wrapper