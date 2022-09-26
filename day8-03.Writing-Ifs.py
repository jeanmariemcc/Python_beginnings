# Joy of coding Day 08 03.Writing-Ifs
# Author JeanMarie McCormack    Composition date: Sept 19, 2022
# Last update: Sept 19, 2022
# Request temperature input from user
# output:
#   temp >90:  "Whoa, it's boiling"
#   90 <= temp >= 80  "It's getting hot"
#   80 < temp >= 60   "A perfect day"
#   60 < temp >=32    "Don't forget your sweater"
#   temp < 32         "Brrr, you need a coat!"

temp = float(input("Enter the current temperature:"))
print()
if temp > 90:
    print("Whoa, it's boiling")
elif temp >= 80:
    print("It's getting hot")
elif temp >= 60:
    print("A perfect day")
elif temp >= 32:
    print("Don't forget your sweater")
else:
    print("Brrr, you need a coat!")

score = float(input("Enter the score from 0-100: "))
print()
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

x = -5 % 5
print("-5 % 5 = ", x)

