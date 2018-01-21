#import mockchain as genechain
import time

#chain = dict([block.hash,block] for block in genechain.chain)

balances = {}

def Event_transfer(observed, sender, receiver, amount):
    global balances
    #if( balances[sender]!=observed.balances[sender]  ):
    #print observed.balances[sender], balances[sender], amount , balances[receiver] , observed.balances[receiver]
    balances[sender] = observed.balances[sender]
       # balances[receiver] = observed.balances[receiver]


    return {sender, receiver, amount}


def watch_gen_accounts(observed,num):
    global balances
    balances= observed.balances






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
