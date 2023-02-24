import time


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


print(sumDigits(154843))
