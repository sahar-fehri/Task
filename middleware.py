#import mockchain as genechain
import time

#chain = dict([block.hash,block] for block in genechain.chain)

balances = {}
Transactions={};
i=0;

def Event_transfer(observed, sender, receiver, amount):
    global balances
    balances[sender] = observed.balances[sender]
    balances[receiver] = observed.balances[receiver]
    #Transactions[]
    #Transactions[0]=
    return {sender, receiver, amount}


def watch_gen_accounts(observed,num):
    global balances
    balances= observed.balances.copy()

def return_list_balances():
    #print balances.values();
    return balances;

def getmedian():
    return sorted(balances.values())[len(balances) / 2]







# def getLongestChain():
#     longestChain={}
#     lastBlock = chain[chain.keys()[0]];
#     lastBlockIndex = 0;
#     for block in chain.values():
#         if(block.number>lastBlockIndex):
#             lastBlock = block
#             lastBlockIndex = block.number
#     for index in range(lastBlock.number):
#         longestChain[lastBlock.hash] = lastBlock
#         lastBlock = chain.get(lastBlock.prevhash)
#     return longestChain
#
#
#
# longest = getLongestChain()
#
#
# def getCurrentMedian(block):
#     return block.accounts.median()
#
# def getlastBlock(Chain):
#     lastBlockIndex=0;
#     lastBlock = Chain.values()[0];
#     for block in Chain.values():
#         if(block.number>lastBlockIndex):
#             lastBlock = block
#             lastBlockIndex = block.number
#     return lastBlock
#
# lastBlock = getlastBlock(longest)
# median = getCurrentMedian(lastBlock)
# print median
# print [(elem.prevhash,elem.hash) for elem in sorted(longest.values(),key = lambda block:block.number)]