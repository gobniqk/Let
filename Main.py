import time
import math


def timeit(minimalized=False, runs=1):
    def decorator(function):
        class color:
            PURPLE = '\033[95m'
            CYAN = '\033[96m'
            DARKCYAN = '\033[36m'
            BLUE = '\033[94m'
            GREEN = '\033[92m'
            YELLOW = '\033[93m'
            RED = '\033[91m'
            BOLD = '\033[1m'
            UNDERLINE = '\033[4m'
            END = '\033[0m'

        def wrapper(*arg):
            length = 0
            for _ in range(runs):
                start = time.perf_counter()
                function(*arg)
                length += time.perf_counter()-start
            length /= runs
            func = function(*arg)
            if not minimalized:
                header = f"{color.BOLD}{color.UNDERLINE}{color.RED}{function.__name__} data:{color.END}"
                return f"{header}\nOutput: {func}\nAverage processing time over {runs:,} runs:{length*1000: .4f}ms\n"
            return f"{function.__name__}: {func} | {length*1000:.4f}ms"

        return wrapper
    return decorator


@timeit(runs=10)
def sumDigits(num: int) -> int:
    digitSum = 0
    while num > 0:
        digitSum += num % 10
        num //= 10
    return digitSum


class Date:

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def compare(self, d1: 'Date'):
        def sign(x): return math.copysign(1, x) if x != 0 else 0
        dayDiff = sign(self.day-d1.day)
        monthDiff = sign(self.month-d1.month)*10
        yearDiff = sign(self.year-d1.year)*100
        return int(sign(dayDiff+monthDiff+yearDiff))


def hello():
    return "hello world"