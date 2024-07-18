def fibonacci_series(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

n = int(input("Enter the number of terms in the Fibonacci series: "))
fib_series = fibonacci_series(n)

print(f"The first {n} terms of the Fibonacci series are:")
for num in fib_series:
    print(num)
