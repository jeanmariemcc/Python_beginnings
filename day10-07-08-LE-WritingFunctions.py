# Joy of coding Day 10 07.LE-Writing-Functions
# Author JeanMarie McCormack    Composition date: Sept 20, 2022
# Last update: Sept 20, 2022
import math


def is_even():
    myNum = eval(input("Input an integer: "))
    if myNum % 2 == 1:
        print("Your number is odd")
    else:
        print("Your number is even")


# is_even()

def is_teachers_even(n):
    return n % 2 == 0


print("Is 4 even?", is_teachers_even(4))
print("Is 5 even?", is_teachers_even(5))


def calculate_total(meal, tax_rate, tip_rate):
    total = meal + meal * tax_rate + meal * tip_rate
    print("Your total is:", round(total, 2))


calculate_total(53.48, 0.07, 0.18)


def hey(myNum):
    print(myNum**2)


hey(5)
hey(0)
hey(-3)


def are_we(repeat, myWord):
    phrase = "Are we " + myWord + " there yet? "
    print(phrase * repeat)


are_we(2, "there")
are_we(3, "50")
are_we(1, "")
are_we(0, "hey!")


def there(exp):
    return float(2 ** exp)


print(there(5))
print(there(-3))


def test_helper(actual, expected):
    if actual == expected:
        print(actual, "PASSED")
    else:
        print("ERROR: actual of:", actual, "!= to expected of:", expected)


def has_it(in_string, letter):
    return letter in in_string


test_helper(has_it("hello", "E"), False)
test_helper(has_it("hello", "e"), True)


def discriminant(a, b, c):
    if 4 * a * c > b ** 2:
        return 0
    else:
        return float(math.sqrt(b ** 2 - 4 * a * c))


test_helper(discriminant(4, 5, 6), float(0))
test_helper(discriminant(2, -4, 10), float(0))
test_helper(discriminant(6, 15, 3), float(12.36931687685298))
test_helper(discriminant(4, 10, -2), float(11.489125293076057))


def quadratic(a, b, c ):
    x1 = float(((-1 * b) - discriminant(a, b, c))/(2 * a))
    x2 = float(((-1 * b) + discriminant(a, b, c))/(2 * a))
    print("x1 = ", x1, "   x2 = ", x2)


quadratic(6, 15, 3)



