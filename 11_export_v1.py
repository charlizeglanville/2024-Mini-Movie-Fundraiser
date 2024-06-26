import pandas as pd
import random
from datetime import date

# lists to hold ticket details
all_names = ["a", "b", "c", "d", "e"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": surcharge
}
# create frame
mini_movie_frame = pd.DataFrame(mini_movie_dict)

# calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']

# Assuming profit is calculated as the ticket price minus a fixed cost per ticket (e.g., 5.00)
fixed_cost_per_ticket = 5.00
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - fixed_cost_per_ticket

# calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# choose winner and look up total won
winner_name = random.choice(all_names)
win_index = all_names.index(winner_name)
total_won = mini_movie_frame.at[win_index, 'Total']

# set index at end (before printing)
mini_movie_frame = mini_movie_frame.set_index('Name')

# **** Get Current data for heading and filename ****
# get today's date
today = date.today()

# get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

heading = "---- Mini Movie Fundraiser Ticket Data ({}/{}/{}) ----\n".format(day, month, year)
filename = "MMF_{}_{}_{}".format(year, month, day)

# currency formatting function
def currency(x):
    return "${:.2f}".format(x)

# Currency Formatting (uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# change frame to a string, so we can export it to file
mini_movie_string = mini_movie_frame.to_string()

# create strings for printing
ticket_cost_heading = "\n---- Ticket Cost / Profit ----"
total_ticket_sales = "Total Ticket Sales: ${:,.2f}".format(total)
total_profit = "Total Profit: ${:,.2f}".format(profit)

# edit text below!!! It needs to work if we have unsold tickets
sales_status = "\n**** All the tickets have been sold ****"

winner_heading = "\n---- Raffle Winner----"
winner_text = "The winner of the raffle is {}. They have won ${:,.2f}. Their ticket is free!".format(winner_name, total_won)

# list holding content to print / write to file
to_write = [heading, mini_movie_string, ticket_cost_heading,
            total_ticket_sales, total_profit, sales_status,
            winner_heading, winner_text]

# print output
for item in to_write:
    print(item)

# write output to file
# create file to hold data (add .txt extension)
write_to = "{}.txt".format(filename)
with open(write_to, "w") as text_file:
    for item in to_write:
        text_file.write(item)
        text_file.write("\n")
