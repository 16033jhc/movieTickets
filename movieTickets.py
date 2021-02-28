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

## Start of loop
# Initialise loop so it runs at least once
name = ""
count = 0 # change to 150 on compeletion of project
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:
    print("You have {} seats left."
        .format(MAX_TICKETS - count))
    
    #Get details
    name = not_blank("Name: ")
    count += 1
    print()

if count == MAX_TICKETS:
    print("You have sold all the available tickets.")
else:
    print("You have sold {} tickets. \n"
        "There are {} places still available"
        .format(count, MAX_TICKETS - count))
# Age (between 12 and 130)

# Calculate ticket price

# Loop for snacks

# Calculate snack price

# Payment Method (and add surcharge for credit card)

# Math for total price

# Profit?

# Data Output to file