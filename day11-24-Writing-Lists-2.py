# Joy of coding Day 11 24-Writing-Lists-2
# Author JeanMarie McCormack    Composition date: Sept 22, 2022
# Last update: Sept 22, 2022

def who_to_vote_for():
    years = eval(input("Enter the candidate's years of experience: "))
    if 5 <= years < 21:
        agree = eval(input("On what percentage of the issues do you and the candidate agree: "))
        if agree >= 80:
            return "Vote for this candidate"
    else:
        return "Do not vote for this candidate"


print(who_to_vote_for())
