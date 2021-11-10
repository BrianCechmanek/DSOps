from time import perf_counter, time, process_time


def benchmark(func):
    ''' Standard benchmarking decorator. '''

    # because wrapper has to be totally 
    # generic, allow any *args, **kwargs
    def wrapper(*args, **kwargs):
        # start the counter (add extra behaviour)
        t = perf_counter()
        
        # pass along all *args, **kwargs to func()
        # so the wrapper is just a pass-through 
        # do not change it's behaviour!
        res = func(*args, **kwargs)
        
        # end the counter/print (add extra behaviour)
        print("Method name:", 
                f"{func.__name__ : <20}", 
            "time to execute: ", 
            f"{perf_counter()-t : >10}s")
        return res

    return wrapper


def benchmark_many(func, iters:int=333):
    ''' Benchmarking decorator for 333 runs. '''

    def wrapper(*args, **kwargs):
        # (add extra behaviour)
        t = perf_counter()
        
        # note the scope of iters
        for i in range(iters):
            # run the function, unmodified
            res = func(*args, **kwargs)
        
        # (add extra behaviour)
        print("Method name:", 
                f"{func.__name__ : <20}", 
                f"time to execute {iters} times:", 
                f"{perf_counter()-t : >10}s")
        return res

    return wrapper