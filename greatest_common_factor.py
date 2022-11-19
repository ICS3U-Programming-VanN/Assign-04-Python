#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: November 9, 2022
# This program asks the user how many numbers they plan on finding
# the greatest common factor of.
# This program will then ask the user if they want to run the program again


# This function returns the greatest common factor of a list of numbers
def find_greatest_factor(numbers, highest_num):
    # Initialize Variable
    common_factors = []

    # Iterates through for each index/number in the list of numbers
    for index in range(0, len(numbers)):
        # Find the factors of each index
        for counter in range(1, highest_num + 1):
            # IF the index is evenly divisible by the incrementing counter
            if numbers[index] % counter == 0:
                # Adds the number/factor to the common_factors list
                common_factors.append(counter)

    # Iterates through for each index/number in the list of numbers
    for index in range(0, len(numbers)):
        # Goes through the factors of the indexes
        for counter in range(1, highest_num + 1):
            # IF there are factors in the common_factors list that an index does not have
            if numbers[index] % counter != 0 and counter in common_factors:
                # Ensures that all wrong factors are removed
                while counter in common_factors:
                    # Removes all unshared factors
                    common_factors.remove(counter)

    # Returns the greatest common factor
    return max(common_factors)


def main():
    # Repeats program until inputted otherwise (Do-While Workaround)
    while True:
        # Initialize Variables
        highest_input = 0
        run_again = ""
        counter = 0

        # List Initialized (meant to contain all numbers user wants to find the GCF of)
        all_numbers = []

        # Checks for exceptions
        try:
            # Asks user for all the numbers they plan to find the GCF of
            total_numbers = int(
                input(
                    "How many numbers do you plan to find the greatest common factor of?: "
                )
            )

            # Checks if the total numbers is negative
            if total_numbers <= 0:
                print("Please enter a positive number for the amount of numbers.\n")

                # Returns to beginning of loop
                continue

        # In the event of an exception
        except Exception:
            print("You must enter positive number!\n")

        else:
            # Gets as many numbers wanted to input (total numbers)
            while counter < total_numbers:

                # Checks for exceptions
                try:
                    # Asks user for the number they wanted to find the factor for
                    user_number = int(input("Enter the number: "))

                # In the event of an exception
                except Exception:
                    print("You must enter a positive number!\n")
                else:
                    # IF the user inputted a negative number
                    if user_number <= 0:
                        print("You must enter a positive number!\n")
                    # IF the user inputted a valid number
                    else:
                        # Adds user's number to the list
                        all_numbers.append(user_number)

                        # Increments counter
                        counter += 1

            # Finds the highest number in the all_numbers list (for function call)
            highest_input = max(all_numbers)

            # Displays the Greatest Common Factor to the user
            print(
                "The greatest common factor of your numbers: "
                + str(find_greatest_factor(all_numbers, highest_input))
            )

            # Continues to ask user if they want to run again (until valid input)
            while True:

                # Asks user if they want to run the program again
                run_again = input(
                    "Do you want to use the program again? (Enter 'y' to run again or 'n' to end the program): "
                )

                # Makes user input into lowercase (to account for case sensitivity)
                run_again = run_again.lower()

                # Exits loop that continues to ask them if they want to run again
                if run_again == "y" or run_again == "n":
                    break

            # Exits loop and ends program if the user wanted to end
            if run_again == "n":
                break


if __name__ == "__main__":
    main()
