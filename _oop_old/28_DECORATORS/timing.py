# Let's define a speed_test decorator
from functools import wraps
from time import time

duration = 90000000


def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Executing {fn.__name__}")
        print(f"Time Elapsed: {end_time - start_time}")
        return result

    return wrapper


@speed_test
def sum_nums_gen():
    return sum(x for x in range(duration))


@speed_test
def sum_nums_list():
    return sum([x for x in range(duration)])


print(sum_nums_gen())
print(sum_nums_list())
