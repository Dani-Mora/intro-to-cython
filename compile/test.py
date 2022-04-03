from sort import quicksort
from utils import time_avg, N
import random


@time_avg
def sort_sample() -> None:
    x = [random.randint(0, N) for _ in range(N)]
    _ = quicksort(x)


print(f"Lapsed {sort_sample():.2f} seconds, on average")
