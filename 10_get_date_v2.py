from datetime import date

#get  today's date
today = date.today()

# Get day, month and year as individual strings
day = today.striftime("%d")
month = today.strftime("%m")
year = today.striftime("%Y")

heading = "The current date is {}/{}/{}".format(day, month, year)
filename = "MMF_{}_{}_{}".format(year, month, day)

# Heading
print(heading)
print("The filename will be {}.txt".format(filename))
