# Joy of coding Day 14 23.files
# Author JeanMarie McCormack    Composition date: Sept 23, 2022
# Last update: Sept 23, 2022

def read_file(file_name):
    dataFile = open(file_name)
    for line in dataFile:
        print("-" + line, end="")
    dataFile.close()


def add_file():
    file_name = input("Enter the name of a file e.g. myFile.txt: ")
    data_file = open(file_name, "w")
    digit = eval(input("Enter a number, or enter a 0 (zero) when finished: "))
    while digit != 0:
        print(digit, file=data_file)
        # file_name.write(digit)
        digit = eval(input("Enter a number, or enter a 0 (zero) when finished: "))
    data_file.close()
    data_file = open(file_name)
    for line in data_file:
        print(line, end="")
    data_file.close()


def read3_files(filename1, filename2, filename3):
    # this assumes the files are in the current directory
    file_list = [filename1, filename2, filename3]
    outputfile = open("day14counts.txt", "w")
    total_lines = 0
    total_words = 0
    for file in file_list:
        line_count = 0
        word_count = 0
        for line in open(file):
            line_count += 1
            word_count += len(line.split(" "))
        total_lines += line_count
        total_words += word_count
        print(file + " : " + str(line_count) + " lines, " + str(word_count) + " words", file=outputfile)
    print("TOTAL: " + str(total_lines) + " lines, " + str(total_words) + " words", file=outputfile)
    outputfile.close()


def main():
    #read_file("day14TextFile.txt")
    #add_file()
    read3_files("day14test1.txt", "day14test2.txt", "day14test3.txt")


main()
