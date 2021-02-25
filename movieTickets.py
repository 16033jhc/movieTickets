# Imports

# Functions
# Checks ticket name is not blank, if blank function shows error
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print("Sorry - this can't be blank.")

###### Main Routine ######

# Dictionaries / Lists for data storage

# Offer first time users a walkthrough of the program

# Loop for ticket details
name = ""
count = 0 # change to 150 on compeletion of project
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:
    name = input("Name: ")
    count += 1
# Name (can't be blank)
#name = not_blank("Name: ")

# Age (between 12 and 130)

# Calculate ticket price

# Loop for snacks

# Calculate snack price

# Payment Method (and add surcharge for credit card)

# Math for total price

# Profit?

# Data Output to file