# Joy of coding Day 09 So You Want To Write Functions
# Author JeanMarie McCormack    Composition date: Sept 19, 2022
# Last update: Sept 19, 2022


def pyramid(char, repeat):
    for i in range(1, repeat + 1):
        print(char * i)


pyramid("#",12)
pyramid("+", 2)
pyramid("I love YOU!! ", 5)


def absDiff(num1, num2):
    return abs(num1 - num2)


print(absDiff(2, -3))