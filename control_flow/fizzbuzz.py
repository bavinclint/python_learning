# write a fizzbuzz function where:
# any number divisible by 3 print Fizz
# any number dividible by 5 print Buzz
# both numbers divisible by 5 & 3 print FizzBuzz
# any other number print the number

def fizz_buzz(number=int(input("Enter number: "))):
    """ a fizzbuzz function that print fizz or buzz or fizzbuzz or number"""
    if (number % 3 == 0) and (number % 5 == 0):
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return number


print(fizz_buzz())
