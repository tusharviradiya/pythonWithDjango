# recursion
# recursion is a function

# how to create recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)