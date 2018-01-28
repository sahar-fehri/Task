import json
import os

import middleware

global chainexist
chainexist = False;

print chainexist


### FUNCTIONS ###

def display_title_bar():
    # Clears the terminal screen, and displays a title bar.
    os.system('clear')

    print("\t**********************************************")
    print("\t***  Hello brainBot App   ***")
    print("\t**********************************************")


def get_user_choice():
    # Let users know what they can do.
    print("\n[1] Initiate Transaction")
    print("[2] Print Balances.")
    print("[3] Print Median")
    print("[4] Print all Transactions")
    print("[5] Print block By Transaction")
    print("[q] Quit.")

    return raw_input("What would you like to do? ")


def initiate_chain():
    # initiate chain
    inp = []
    inp.append(raw_input("Enter chain height."))
    inp.append(raw_input("Enter revert probability."))
    inp.append(raw_input("Enter number of accounts."))
    inp.append(raw_input("Enter max transaction per block."))
    middleware.initiate_chain(int(inp[0]), float(inp[1]), int(inp[2]), int(inp[3]))
    global chainexist
    chainexist = True


def getBalances():
    print chainexist
    if (chainexist):
        print json.dumps(middleware.return_list_balances(), indent=4, sort_keys=True)
    else:
        print "No chain was previously initiated!"


def getMedian():
    if chainexist == True:
        print "median is " + str(middleware.getmedian())
    else:
        print "No chain was previously initiated!"


def getAllTransactions():
    if chainexist == True:
        print json.dumps([b.serialize(include_balances=False) for b in middleware.getLongestChain().values()], indent=4,
                         sort_keys=True)
    else:
        print "No chain was previously initiated!"


def getBlockById():
    if chainexist == True:
        id = raw_input("Enter id transaction")
        block, long = middleware.getBlockByTransactionId(id)
        if (block):
            print json.dumps(block.serialize(), indent=4, sort_keys=True)
            print " Number of confirmations is :", long
        else:
            print "invalid id"
    else:
        print "No chain was previously initiated!"


def quit():
    # This function dumps the names into a file, and prints a quit message.
    print("\nThanks for playing.")


### MAIN PROGRAM ###
# Set up a loop where users can choose what they'd like to do.


choice = ''
display_title_bar()
while choice != 'q':

    choice = get_user_choice()

    # Respond to the user's choice.
    display_title_bar()
    if choice == '1':
        initiate_chain()
    elif choice == '2':
        getBalances()
    elif choice == '3':
        getMedian()
    elif choice == '4':
        getAllTransactions()
    elif choice == '5':
        getBlockById()
    elif choice == 'q':
        quit()
        print("\nThanks for playing. Bye.")
    else:
        print("\nI didn't understand that choice.\n")