# Author: JD 12/03/2021

def mul_3():
    for number in [2, 4, 6, 9, 10, 12, 13, 14]:
        if number % 2 != 0:
            continue
        print(number)
    print("Done")
mul_3()