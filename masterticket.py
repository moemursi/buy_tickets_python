import sys

TICKET_PRICE = 10

tickets_remaining = 100

# Run this code only if there is tickets remaining
while tickets_remaining >= 1:
    # output how many tickets are remaining using tickets_remaining
    print ("There are {} tickets remaining".format(tickets_remaining))

    #gather username and assign to avariable
    name = input("What is your name :  ")
   
    num_tickets = input("How many tickets you would like to purchase {} : ".format(name))
    #expect value error to happen and handle it appropriately
    try:
        num_tickets = int(num_tickets)
        #RAISE VALUE ERROR IF REQUEST FOR MORE TICKETS THAN THE AVAILABLE
        if num_tickets > tickets_remaining or num_tickets <1:
            raise ValueError("There are only {} tickets remaining ".format(tickets_remaining))
    except ValueError as err:
        #inclue the error text in the output

        print("INVALID ENTRY ,{}, PLEASE RETRY ...  ".format(err))
    else:
        #calculate the price ( number of tickets * price per ticket) assign to avariable 
        amount_due = num_tickets * TICKET_PRICE
        # output the price to screen 
        print ("Total Due is ${}".format(amount_due))
        #prompt user if they want to continue
        should_proceed = input("Do you want to proceed ? Y/N ")
        #if they want to proceed
        if should_proceed.lower() == "y":
            #print out SOLD to confirm purchase
            #TO DO : Gather payment info and process it 
                print("SOLD ! ")
                #then decrement number of tickets by the amount purchased
                tickets_remaining -= num_tickets
                

            # thank the customer
        else:
                print("Thank you anyways, {}!.".format(name))
        #notify the user if all tickets are sold 
print("Tickets are sold out !!! ")