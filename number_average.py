#!/usr/bin/env python3

# Created by: Jenoe Balote
# Created on June 2021
# This program finds the average of 10 random numbers from 1-100

import random


def main():
    # this function averages 10 numbers

    random_numbers = []

    # process and output
    print("Generating numbers...")
    print("")
    for loop_counter in range(0, 10):
        number_created = random.randint(1, 100)
        random_numbers.append(number_created)
    num_average = 0
    for loop_counter in range(len(random_numbers)):
        print("The random number {0} is {1}.".format(
            loop_counter + 1, random_numbers[loop_counter]))
        num_average += random_numbers[loop_counter]
    num_average = num_average / len(random_numbers)
    print("\nThe average of the numbers is: {}.".format(num_average))
    print("\nDone.")


if __name__ == "__main__":
    main()
