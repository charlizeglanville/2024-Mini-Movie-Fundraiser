#functions go here
def cash_credit(question):

    while True:
        response = input(question).lower()

        if response == "cash" or response =="ca":
            return "Cash"

        elif response == "credit" or response =="cr":
            return "Credit"

        else:
            print("Please choose a valid payment method.")
# main routine goes here
while True:

    payment_method = cash_credit("Choose a payment method (cash"" or credit): ")

    print ("You chose", payment_method,".")

print ("program continues ...")
print()