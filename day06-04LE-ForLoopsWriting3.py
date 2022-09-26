# Joy of coding Day 06 04.LE-ForLoopsWriting3
# Author JeanMarie McCormack    Composition date: Sept 18, 2022
# Last update: Sept 18, 2022


for i in range(-16, 16, 4):
    print(i, end="-")
#print("16")
result =i+4
print(result)
print("*" * 10)

print("i = ", i)

for i in range(-10,100,10):
    print(i, end="... ")
print("100")

mySum = 0
for i in range(5):
    mySum += int(input("Enter a grade:"))
print("Current average:", mySum/5)
print("25% improvement:", mySum/5*1.25)

saying = "howdy"
for u in saying.upper():
    print(saying, end="!! ")
