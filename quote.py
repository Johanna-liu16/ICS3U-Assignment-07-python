#!/usr/bin/env python3

# Created by: Johanna Liu
# Created on: Dec 2022
# This program calculates the average


def create_frame(words):
    # This function creates a frame that matches the quote
    # With help from: https://stackoverflow.com/questions/4057129/border-around-string-python
    largest_string = words[0]
    height = len(words)
    space = ""
    lines = []

    for loop_counter in range(len(words)):
        if len(words[loop_counter]) > len(largest_string):
            largest_string = words[loop_counter]
    width = len(largest_string) + 4

    border = ""
    for loop_counter in range(width):
        border += "#"

    for counter in range(height):
        extra_spaces = width - len(words[counter]) - 3
        for counter_1 in range(extra_spaces):
            space += " "
        line = "# {0}{1}#".format(words[counter], space)
        lines.append(line)
        space = ""

    return border, lines, border

def main():
    # this function uses an array
    words = []
    quote = None

    # input
    print("This program frames a quote.")
    quote = input("Enter what would you like to write: ")
    print("")

    # process
    words = quote.split(" ")

    tuple = create_frame(words)
    print(tuple[0])
    for loop_counter in range(len(tuple[1])):
        print(tuple[1][loop_counter])
    print(tuple[2])

    print("\nDone.")


if __name__ == "__main__":
    main()
