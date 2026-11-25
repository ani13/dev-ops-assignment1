
def fibonacci(n):
    sequence = []

    a, b = 0, 1

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence


number = 10

result = fibonacci(number)

print(f"First {number} Fibonacci numbers:")
print(result)
