def why(list_w):
    y = 1
    j = 0
    while j < len(list_w) and y < 11:
        x = list_w[j]
        if x < 0:
            y -= x
        elif x % 2 == 0:
            y *= x
        else:
            y += x
        j += 2
        print(y)
    return y


# print(why([4, -1, -5, 2, 1, 3, 7, -8]))


def find_u():
    string = (input("Input a string or short phrase: "))
    return string.upper().find("U")


print("Index of first 'u' or 'U' in your phrase is (or -1 if not found) ", find_u())


def average_vowels(the_list):
    """Write a function average_vowels that takes a list of
    strings as a parameter and returns the average number of
    vowels occurring in each string in the list, both upper - &
    lower - cased.No library functions aside from input / output.
    """
    vowels = ["A", "E", "I", "O", "U"]
    vowel_count = 0
    for item in the_list:
        for v in vowels:
            vowel_count += item.upper().count(v)
    return vowel_count / len(the_list)


def avg_vowels2(the_list):
    vowels = ["A", "E", "I", "O", "U"]
    vowel_count = 0
    i = 0
    while i < len(the_list):  # included a while just for you
        item = the_list[i]
        for char in list(item):  # split the string into a list of characters
            for v in vowels:
                if char.upper() == v:
                    vowel_count += 1
        i += 1
    return vowel_count / len(the_list)


test_list = (["Zebra", "lightsaber", "1234 JOYS!"])
print("First function: Average number of vowels in the strings in your list is:", average_vowels(test_list))
print()
print("Second function: Average number of vowels in the strings in your list is:", avg_vowels2(test_list))

