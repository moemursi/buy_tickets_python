import sys

TICKET_PRICE = 10
SERVICE_CHARGE = 2
tickets_remaining = 100

def calculate_price(num_tickets):
    return (num_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:
    print ("There are {} tickets remaining".format(tickets_remaining))
    name = input("What is your name :  ")
    num_tickets = input("How many tickets you would like to purchase {} : ".format(name))
    try:
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining or num_tickets <1:
            raise ValueError("There are only {} tickets remaining ".format(tickets_remaining))
    except ValueError as err:
        print("INVALID ENTRY ,{}, PLEASE RETRY ...  ".format(err))
    else:
        amount_due = calculate_price(num_tickets)
        print ("Total Due is ${}".format(amount_due))
        should_proceed = input("Do you want to proceed ? Y/N ")
        if should_proceed.lower() == "y":
                print("SOLD ! ")
                tickets_remaining -= num_tickets  
        else:
                print("Thank you anyways, {}!.".format(name))
print("Tickets are sold out !!! ")