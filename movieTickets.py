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
ticketCount = 0
ticketSales = 0
MAX_TICKETS = 5 # change to 150 on compeletion of project

while name != "xxx" and ticketCount < MAX_TICKETS:
    # Tells the user how many seats are left
    if ticketCount < MAX_TICKETS - 1:
        print("You have {} seats left."
            .format(MAX_TICKETS - ticketCount))
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
        print("You are too young for this movie.")
        continue
    elif age > 130:
        print("Are you sure? This seems like a mistake.")
        continue

    # Calculate ticket sales

    if age < 65:
        ticketPrice = 10.50
    elif age < 16:
        ticketPrice = 7.50
    else:
        ticketPrice = 6.50

    ticketCount += 1
    ticketSales += ticketPrice
    print("Price: ${:.2f}".format(ticketPrice))
    #Ticket Profit
    ticketProfit = ticketSales - (5 * ticketCount)
    print("Profit from Tickets: ${:.2f}.".format(ticketProfit))
    
    # Tell user if there are still unsold tickets
    if ticketCount == MAX_TICKETS:
        print("You have sold all the available tickets.")
    else:
        print("You have sold {} tickets.    \n"
            " There are {} places still available."
                .format(ticketCount, MAX_TICKETS - ticketCount))

#Allows up to the max ticket num to be sold
if ticketCount == MAX_TICKETS:
    print("You have sold all the available tickets.")
else:
    print("You have sold {} tickets. \n"
        "There are {} places still available"
        .format(ticketCount, MAX_TICKETS - ticketCount))

# Calculate ticket price

# Loop for snacks

# Calculate snack price

# Payment Method (and add surcharge for credit card)

# Math for total price

# Profit?

# Data Output to file