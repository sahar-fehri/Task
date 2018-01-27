import random
import mockchain
import middleware
import os
import json

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
    print("[q] Quit.")

    return raw_input("What would you like to do? ")


def initiate_chain():
    # initiate chain
    inp = []
    inp.append(raw_input("Enter chain height."))
    inp.append(raw_input("Enter revert probability."))
    inp.append(raw_input("Enter number of accounts."))
    inp.append(raw_input("Enter max transaction per block."))
    random.seed(43)
    chain = mockchain.gen_chain(height=int(inp[0]), p_revert=float(inp[1]), num_accounts=int(inp[2]), max_transfers=int(inp[3]))
    serialized_blocks = [b.serialize(include_balances=False) for b in chain]
    # random.shuffle(serialized_blocks)
    # print json.dumps(serialized_blocks, indent=4, sort_keys=True)
    # print 'blocks: {} max reverted:{}'.format(len(chain), longest_revert(chain))
    #
    txs = []
    for block in set(chain):
        txs.extend(block.transfers)
    print 'total transfers:{} unique transfers:{}'.format(len(txs), len(set(txs)))



def get_Balances():
    print json.dumps(middleware.return_list_balances())

def getmedian():
    print "median is 2" +str(middleware.return_median())

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
        get_Balances()
    elif choice == '3':
        getmedian()
    elif choice == 'q':
        quit()
        print("\nThanks for playing. Bye.")
    else:
        print("\nI didn't understand that choice.\n")