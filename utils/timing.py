import time


def time_avg(func, n=10):
    def wrapper(*args, **kwargs):
        """Returns average execution time for the input function"""
        summed = 0
        for _ in range(n):
            before = time.time()
            func(*args, **kwargs)
            after = time.time()
            summed += after - before
        return summed / n

    return wrapper
