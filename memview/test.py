from sort import quicksort
from utils import time_avg, N

import numpy as np


@time_avg
def sort_sample() -> None:
    x = np.random.randint(0, N, size=(N,)).astype("int32")
    _ = quicksort(x)


print(f"Lapsed {sort_sample():.2f} seconds, on average")
