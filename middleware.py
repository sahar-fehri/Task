
import random

balances = {}
chain = []
myChain = {}


def Event_transfer(observed, sender, receiver, amount):
    global balances
    balances[sender] = observed.balances[sender]
    balances[receiver] = observed.balances[receiver]
    return {sender, receiver, amount}


def watch_gen_accounts(observed, num):
    global balances
    balances = observed.balances.copy()


def return_list_balances():
    return balances;


def getmedian():
    return sorted(balances.values())[len(balances) / 2]


def initiate_chain(height, p_revert, num_accounts, max_transfers):
    # initiate chain
    from mockchain import gen_chain

    random.seed(43)
    global myChain
    chain = gen_chain(height=height, p_revert=p_revert, num_accounts=num_accounts,
                      max_transfers=max_transfers)

    myChain = dict([block.hash, block] for block in chain)
    txs = []
    for block in set(chain):
        txs.extend(block.transfers)
    print 'total transfers:{} unique transfers:{}'.format(len(txs), len(set(txs)))


def getLongestChain():
    longestChain = {}
    lastBlock = myChain[myChain.keys()[0]];
    lastBlockIndex = 0;
    for block in myChain.values():
        if (block.number > lastBlockIndex):
            lastBlock = block
            lastBlockIndex = block.number
    for index in range(lastBlock.number):
        longestChain[lastBlock.hash] = lastBlock
        lastBlock = myChain.get(lastBlock.prevhash)
    return longestChain


def getBlockByTransactionId(_id):
    longest = getLongestChain()
    for block in longest.values():
        for transfer in block.transfers:
            if (transfer.id == _id):
                return block, len(longest) - block.number




                # def getlastBlock(Chain):
                #     lastBlockIndex=0;
                #     lastBlock = Chain.values()[0];
                #     for block in Chain.values():
                #         if(block.number>lastBlockIndex):
                #             lastBlock = block
                #             lastBlockIndex = block.number
                #     return lastBlock