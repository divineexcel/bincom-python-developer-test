import random

# Bincom Python Basic Developer Test
# Bonus and Additional Questions

# Question 7: Recursive Search
# Question 8: Random 4-digit binary number to base 10
# Question 9: Sum of first 50 Fibonacci numbers



def recursive_search(numbers, target, index=0):
    if index == len(numbers):
        return False

    if numbers[index] == target:
        return True

    return recursive_search(numbers, target, index + 1)


numbers = [10, 20, 30, 40, 50]

target = int(input("Enter a number to search for: "))

result = recursive_search(numbers, target)

print("Found:", result)


# Question 8: Random 4-digit binary number

binary_number = ""

for i in range(4):
    binary_number += str(random.randint(0, 1))

print("Random binary number:", binary_number)

decimal_number = int(binary_number, 2)

print("Base 10:", decimal_number)


# Question 9: Sum of the first 50 Fibonacci numbers

a = 0
b = 1
total = 0

for i in range(50):
    total += a
    a, b = b, a + b

print("Sum of the first 50 Fibonacci numbers:", total)