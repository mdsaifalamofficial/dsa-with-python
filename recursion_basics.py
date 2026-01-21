# RECURSION BASICS

# Example 1: Print numbers using recursion
def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n)

print_numbers(5)


# Example 2: Factorial using recursion
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))
