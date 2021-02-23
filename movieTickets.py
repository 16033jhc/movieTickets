# Imports

# Functions

def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print(error_message)

###### Main Routine ######

# Dictionaries / Lists for data storage

# Offer first time users a walkthrough of the program

# Loop for ticket details

# Name (can't be blank)
name = not_blank("Name: ",
                "Sorry - this can't be blank, "
                "please enter your name.")

# Age (between 12 and 130)

# Calculate ticket price

# Loop for snacks

# Calculate snack price

# Payment Method (and add surcharge for credit card)

# Math for total price

# Profit?

# Data Output to file