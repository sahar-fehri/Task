import random
import mockchain
import  middleware
def initiate_chain():
    random.seed(43)
    chain = mockchain.gen_chain(height=10, p_revert=0.5, num_accounts=2, max_transfers=2)
    serialized_blocks = [b.serialize(include_balances=False) for b in chain]
    # random.shuffle(serialized_blocks)
    # print json.dumps(serialized_blocks, indent=4, sort_keys=True)
    # print 'blocks: {} max reverted:{}'.format(len(chain), longest_revert(chain))
    #
    txs = []
    for block in set(chain):
        txs.extend(block.transfers)
    print 'total transfers:{} unique transfers:{}'.format(len(txs), len(set(txs)))
def getBlances():
    print middleware.balances,'appp'
initiate_chain()
