# Joy of coding Day 11 26-Writing-Lists-3
# Author JeanMarie McCormack    Composition date: Sept 22, 2022
# Last update: Sept 22, 2022

def avg_evens(num_list):
    even_list = []
    for num in num_list:
        if num % 2 == 0:
            even_list.append(num)
    return sum(even_list) / len(even_list)


#print(avg_evens([-2, -3, -4, 0, 1, 2, 3]))


def match(string1, string2):
    # eliminate duplicate chars in string1 = s1
    s1 = ""
    for char1 in string1:
        if char1 not in s1:
            s1 = s1 + char1
    # eliminate duplicate chars in string2 = s2
    s2 = ""
    for char2 in string2:
        if char2 not in s2:
            s2 = s2 + char2
    # check for matching chars in s1 and s2
    tot_matched = 0
    for c1 in s1:
        if c1.casefold() in s2.casefold():  # if character from s1 is in s2
            tot_matched += 1
    return tot_matched


print("total matching chars:", match("hello", "Healing"))
print("total matching chars:", match("Healing", "hello"))
print("total matching chars:", match("hellllllo", "Heallling"))
print("total matching chars:", match("bcd", "Healing"))


def em_match(string1, string2):
    # eliminate duplicate chars in string1 = s1
    s1 = ""
    for char1 in string1:
        if char1 not in s1:
            s1 = s1 + char1

    # check for matching chars in s1 and string2
    tot_matched = 0
    for c1 in s1:
        if c1.casefold() in string2.casefold():  # if character from s1 is in s2
            tot_matched += 1
    return tot_matched


print("total matching chars:", em_match("hello", "Healing"))
print("total matching chars:", em_match("Healing", "hello"))
print("total matching chars:", em_match("hellllllo", "Heallling"))
print("total matching chars:", em_match("bcd", "Healing"))
