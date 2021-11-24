import random

# Here's another use of decorators: retrying a function n times


def retry(attempts):
    def run_func(func):
        def f():
            tried = 0
            while tried < attempts:
                try:
                    return func()
                except:
                    tried += 1

        return f

    return run_func


@retry(attempts=10)
def foo():
    if random.random() > 0.5:
        print("failed...")
        raise
    else:
        print("ran foo successfully!")
