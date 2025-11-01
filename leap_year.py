#!/usr/bin/env python3
# Created By: Abdul
# Date: 10/30/2025
# Program to ask the user for an integer


def main():
    # get user input and handle exceptions
    try:
        year = input("Please enter a year: ")
        year = int(year)
        # check if the age is within the allowed range
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print(year, "is a leap year.")
                else:
                    print(year, "is not a leap year.")
            else:
                print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")

    # if user input is not an integer, catch the exception
    except ValueError:
        print(year, "is not an integer.")
    # display ending message to user no matter the outcome
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
