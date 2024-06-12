#functions go here

# checks user has entered yes /no to a question:
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response =="y":
            return "yes"

        elif response == "no" or response =="n":
            return "no"

        else:
            print("Please answer yes or no.")

# checks that user response is not blank
def not_blank(question):

    while True:
        response = input(question)

        if response == "" or response ==" ":
            print("Sorry this can't be blank. Please try again!")
        else:
            return response


# Main routine starts here

# Set maximum number of tickets below
MAX_TICKETS = 3
tickets_sold = 0

# ask user of they want to see the instructions

want_instructions = yes_no("Do you want to read the ""instructions? ") .lower()

if want_instructions == "yes" or want_instructions == "y":
        print("Instructions go here")

print()

# Loop to sell tickets
while tickets_sold < MAX_TICKETS:
    name = not_blank("Enter you name (or 'xx' to quit) ")

    if name == 'xx':
        break

    tickets_sold += 1

# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulations, you have sold all the tickets!")
else:
    print("You have sold {} ticket/s. There are {} ticket/s remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))
