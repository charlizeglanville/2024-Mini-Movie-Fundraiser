# functions go here

#checks users enter an integer to a given question
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer.")

# Main routine goes here
ticket_sold = 0

while True:

    name = input("Enter your name / xx to quit: ")

    if name == "xx":
        break

    age = num_check("Age: ")

    if 12 <= age <=120:
        pass
    elif age < 12:
        print("Sorry you are too young for this movie! :(")
        continue
    else:
        print("?? That looks like a typo, please try again. ")
        continue

    ticket_sold +=1