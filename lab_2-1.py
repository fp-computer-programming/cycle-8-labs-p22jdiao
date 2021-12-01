# Author: JD 12/01/2021

num = int(input("Enter the number: "))

def find_sum(number):
    b = 0
    for a in range(number + 1):
        b += a
    
    return b

sum = find_sum(num)

print(sum)
