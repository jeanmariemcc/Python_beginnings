# Joy of coding Day 12 23.WritingWhiles
# Author JeanMarie McCormack    Composition date: Sept 22, 2022
# Last update: Sept 22, 2022


i = 1
while i < 6:
    print(i)
    i += 1

print()
j = 2
while j < 12:
    print(j)
    j += 3

k = -10
while k < 1:
    print(k, end=" ")
    k += 2
print()

ii = 1
while ii < 5:
    print("*" * 4)
    ii += 1

my_string = "CSCI 150"
jj = 0
while jj < len(my_string):
    print(my_string[jj])
    jj += 1

list_sum = 0
user_list = []
user_num = eval(input("Enter a number or 0 (zero) when finished: "))
while user_num != 0:
    user_list.append(user_num)
    user_num = eval(input("Enter a number or 0 (zero) when finished: "))
print(sorted(user_list))
print("Sum:", sum(user_list))
print("Average:", sum(user_list) / len(user_list))



