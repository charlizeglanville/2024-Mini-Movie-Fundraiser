# Main routine starts here

# Set maximum number of tickets below
MAX_TICKETS = 3

# Loop to sell tickets
tickets_sold = 0
while tickets_sold < MAX_TICKETS:
    name = input("Please enter your name or 'xx' to quit: ")

    if name == 'xx':
        break

    tickets_sold += 1

# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulations, you have sold all the tickets!")
else:
    print("You have sold {} ticket/s. There are {} ticket/s remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))
