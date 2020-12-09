#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: December 2020
# This program determines the squares of every number from 0 to your input


def main():
    # This function determines the squares of every number from 0 to your input

    print("")
    print("This program determines the squares of every"
          " number from 0 to your input.")
    print("")
    number_str = input("Positive number: ")
    print("")

    try:
        number = int(number_str)
    except Exception:
        print("Invalid Input")
    else:
        if number > -1:
            for counter in range(number + 1):
                answer = int((counter) ** 2)
                counter_str = str(counter)
                answer_str = str(answer)
                print(counter_str + "²=" + answer_str)
        else:
            print("Please input a positive number instead")


if __name__ == "__main__":
    main()
