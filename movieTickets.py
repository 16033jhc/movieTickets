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

def int_check(question):
    
    error = "Please enter a whole number that is more than 0."

    valid = False
    while not valid:

        try:
            response = int(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

###### Main Routine ######

# Dictionaries / Lists for data storage

# Offer first time users a walkthrough of the program

## Start of loop
# Initialise loop so it runs at least once
name = ""
count = 0 # change to 150 on compeletion of project
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:
    # Tells the user how many seats are left
    if count < 4:
        print("You have {} seats left."
            .format(MAX_TICKETS - count))
    # Warns user that only one seat is left
    else:
        print("##### There is ONE seat left! #####")
    
    #Get details
    
    #Get name (can't be blank)
    name = not_blank("Name: ")
    if name == "xxx":
        break

    # Age (between 12 and 130)
    age = int_check("Age: ")
    
    if age < 12:
        print("You are too young for this movie. \n"
            "Go do homework, kid.")
        continue
    elif age > 130:
        print("Are you sure? This seems like a mistake.")
        continue

    count += 1
if count == MAX_TICKETS:
    print("You have sold all the available tickets.")
else:
    print("You have sold {} tickets. \n"
        "There are {} places still available"
        .format(count, MAX_TICKETS - count))

# Calculate ticket price

# Loop for snacks

# Calculate snack price

# Payment Method (and add surcharge for credit card)

# Math for total price

# Profit?

# Data Output to file