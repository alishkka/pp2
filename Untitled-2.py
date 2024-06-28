def generate_squares(N):
    for i in range(N + 1):
        yield i * i

# Example usage
N = 5
for square in generate_squares(N):
    print(square)

def generate_even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

# Example usage
n = int(input("Enter a number: "))
even_numbers = list(generate_even_numbers(n))
print(",".join(map(str, even_numbers)))

def generate_divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Example usage
n = int(input("Enter a number: "))
for number in generate_divisible_by_3_and_4(n):
    print(number)

def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

# Example usage
a = 3
b = 8
for square in squares(a, b):
    print(square)

def countdown(n):
    while n >= 0:
        yield n
        n -= 1

# Example usage
n = 5
for number in countdown(n):
    print(number)