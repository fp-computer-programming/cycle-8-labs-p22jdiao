# Author: JD 12/02/2021

def sum_to(n):
    total = 0
    counter = 0
    while counter <= n:
        total += counter
        counter += 1
    return total

number = int(input("Input number to sum: "))

result = sum_to(number)

print("the sum to", number, "is", str(result)+".")