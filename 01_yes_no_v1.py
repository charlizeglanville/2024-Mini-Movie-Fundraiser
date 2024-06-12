# functions go here

# main routine goes here
want_instructions = input("Do you want to read the instructions? ")
print(want_instructions)

if want_instructions == "yes" or want_instructions == "y":
    print(want_instructions)
elif want_instructions == "no" or want_instructions == "n":
    pass
else:
    print("Please answer Yes / No")