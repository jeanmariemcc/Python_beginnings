# Joy of coding Day 12 23.WritingWhiles
# Author JeanMarie McCormack    Composition date: Sept 22, 2022
# Last update: Sept 22, 2022

# average_neg_evens - function takes a list of numbers as input,
#  returns the average of all negative even numbers in the list
def average_neg_evens(input_list):
        neg_evens = []
        i = 0
        while i < len(input_list):
            if input_list[i] < 0 and input_list[i] % 2 == 0:
                neg_evens.append(input_list[i])
            i += 1
        return sum(neg_evens) / len(neg_evens)


# count_letter - input: list of strings, string letter
#    output: number of times the string letter (irrespective of case)
#            occurs in the list
def count_letter(in_list, match_letter):
    letter_count = 0
    i = 0
    while i < len(in_list):
        letter_count += in_list[i].upper().count(match_letter.upper())
        i += 1
    return letter_count


def count_zeroes():
    user_num = (input("Enter a number ('Q' to quit)? "))
    zero_count = 0
    while user_num != "Q":
        zero_count += user_num.count("0")
        user_num = (input("Enter a number ('Q' to quit)? "))
    print("You entered", zero_count, "zeroes")


def count_fricatives(my_list):
    fric_list = ["f", "s", "v", "z"]
    fricative_count = 0
    i = 0
    while i < len(my_list):
        j = 0
        while j < len(fric_list):
            fricative_count += my_list[i].lower().count(fric_list[j])
            j += 1
        i += 1
    return fricative_count


def main():
    print("Expected average: -3. Average of list is:", average_neg_evens([0, 1, 2, -2, -3, -4, 3, 4]))
    print()
    list1 = ["HELLO", "goodbye", "1234 Oooh!"]
    print("Expected answer: 6, Number of o's in your list is:", count_letter(list1, "o"))
    list2 = ["HELLO", "NJ", "goodbye", "1234 Oooh!"]
    print(list2[:2])
    my_list = ["Zebra", "lightsaber", "1234 JOYS!"]
    print(count_fricatives(my_list))


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


print(why([4, -1, -5, 2, 1, 3, 7, -8]))

#main()


#count_zeroes()


