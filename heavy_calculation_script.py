import sys

sys.setrecursionlimit(3000)

def fib_memo(n, memo={}):
    """
    Calculate the nth Fibonacci number using memoization to optimize.
    :param n: The nth Fibonacci number to calculate.
    :param memo: Dictionary to store previously calculated Fibonacci numbers.
    :return: The nth Fibonacci number.
    """
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

def heavy_calculation():
    """
    Perform heavy calculations by calculating a large Fibonacci number.
    """
    n = 1000  # Change this value for larger or smaller calculations
    print(f"Calculating the {n}th Fibonacci number...")
    fib_number = fib_memo(n)
    print(f"The {n}th Fibonacci number is: {fib_number}")

if __name__ == "__main__":
    heavy_calculation()
