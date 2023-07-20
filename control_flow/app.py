# tenary operator
# age = 22
# message = "Eligible" if age >= 18 else "Not eligible"
# print(message)

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")
