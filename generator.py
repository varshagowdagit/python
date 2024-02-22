def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Using the generator to print the first 10 Fibonacci numbers
fib_gen = fibonacci_generator()
for _ in range(10):
    print(next(fib_gen))

def even_numbers():
    num = 0
    while num < 10:
        yield num
        num += 2
# Using the generator to print the first 5 even numbers
for num in even_numbers():
    print(num)


def squares_generator(n):
    for i in range(n):
        yield i ** 2
gen = squares_generator(5)

for square in gen:
    print(square)
