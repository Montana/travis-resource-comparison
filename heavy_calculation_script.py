import sys

sys.setrecursionlimit(3000)

def fib_memo(curr, memo={}):
    if curr in memo:
        return memo[curr]
    if curr <= 2:
        return 1
    memo[curr] = fib_memo(curr-1, memo) + fib_memo(curr-2, memo)
    return memo[curr]

def heavy_calculation():
    initial_value = 1000
    increments = 5
    curr = initial_value

    for i in range(increments):
        print(f"Calculating the {curr}th Fibonacci number...")
        fib_number = fib_memo(curr)
        print(f"The {curr}th Fibonacci number is: {fib_number}")
        curr += 500

if __name__ == "__main__":
    heavy_calculation()
