# import random

# number = random.randint(-10, 10)
# if (number > 0):
#     print(f"{number} is positive")
# elif (number < 0):
#     print(f"{number} is negative")
# else:
#     print(number)


# import random
# number = random.randint(-10000, 10000)
# if number < 0:
#     last_digit = int(str(number)[-1]) * -1
# if number > 0:
#     last_digit = int(str(number)[-1])
# else:
#     last_digit == 0
# if last_digit > 5:
#     print(f"Last digit of {number} is {last_digit} and is greater than 5")
# elif last_digit < 6 and last_digit != 0:
#     print(f"Last digit of {number} is {last_digit} less than 6 and not 0")
# else:
#     print(f"Last digit of {number} is {last_digit} is 0")


# for a in "abcdfghijklmnoprstuvwxyz":
#     if a == "q" or a == "e":
#         continue
#     print("{}".format(a), end='')
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
