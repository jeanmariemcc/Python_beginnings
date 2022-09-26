# Joy of coding Day 11 22-Writing-Lists-1
# Author JeanMarie McCormack    Composition date: Sept 22, 2022
# Last update: Sept 22, 2022

def user_20_avg():
    total = 0
    for i in range(20):
        total += eval(input("Input an integer: "))
    print("the average of your 20 inputs is:", round(float(total / 20), 2))


#user_20_avg()


# mangle a string as follows:
# all upper case
# remove every third character
# remove third to last character
def mangle(orig_string):
    string_list = [x for x in orig_string.upper()]   # this also works to unpack the string
    """
        # either this block (which I think is more readable)
        # or the list above produce the same result
        string_list = []
        for letter in orig_string.upper():
            string_list.append(letter)
    """
    del string_list[2]
    del string_list[-3]
    print("".join(string_list))


mangle("abcdefghijkl")
mangle("1234")
mangle("hellothere")
mangle("42 degrees Celsius")
mangle("eeeeeee")


def em_mangle(string):
    string = string.upper()
    return string[:2] + string[3:-3] + string[-2]


print("Emily's", em_mangle("abcdefghijkl"))
print("Emily's", em_mangle("1234"))
print("Emily's", em_mangle("hellothere"))
print("Emily's", em_mangle("42 degrees Celsius"))


def count_e(string_list):
    e_count = 0
    for item in string_list:
     #   e_count += item.count("e")
        e_count += item.upper().count("E")
    print("Your list contains", e_count, "e or E's")


count_e(["e", "E"])
count_e(["hi", "hello", "EEK!"])


def count_vowels(string_list):
    v_count = 0
    vowels = ["A", "E", "I", "O", "U"]
    for item in string_list:
        for v in vowels:
            v_count += item.upper().count(v)
    print("Your list contains", v_count, "vowels")


count_vowels(["hi", "hello", "OOF!"])


