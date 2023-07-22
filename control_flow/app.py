# tenary operator
# age = 22
# message = "Eligible" if age >= 18 else "Not eligible"
# print(message)

# iterate even numbers
# count = 0
# for number in range(1, 10):
#     if number % 2 == 0:
#         count += 1
#         print(number)
# print(f"We have {count} even numbers")

# Fibonacci series:
# the sum of two elements defines the next
# def fib(n=int(input('Enter number: '))):  # return Fibonacci series up to n
#     """Return a list containing the Fibonacci series up to n."""
#     results = []
#     a, b = 0, 1
#     while a < n:
#         results.append(a)
#         a, b = b, a+b
#     return results


# number = print(fib())
# number


# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print("Start")
# print(multiply(1, 2, 3))

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
