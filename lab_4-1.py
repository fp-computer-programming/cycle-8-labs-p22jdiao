# Author: JD 12/03/2021

def adding():
    total = 0
    while True:
        number = int(input("Enter a number: "))
        if number == -1:
            break
        total += number
    
    print(total)

adding()

    
        