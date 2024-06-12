# function goes here

# checks that user response is not blank
def not_blank(question):

    while True:
        response = input(question)

        if response == "" or response ==" ":
            print("Sorry this can't be blank. Please try again!")
        else:
            return response

# main routine goes here
while True:
    name = not_blank("Enter you name (or 'xx' to quit) ")
    if name == "xx":
        break

print("We are done!")
