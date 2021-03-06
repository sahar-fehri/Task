import collections
import hashlib
import random

from observed import event

import middleware


def hexhash(x):
    return '0x' + hashlib.sha224(str(x)).hexdigest()[:6]


TransferEvent = collections.namedtuple('TransferEvent', 'id,sender, receiver, amount')


class Accounts(object):
    initial_supply = 0
    idTransaction = 0

    def __init__(self, num_accounts=0, copy_from=None):
        self.balances = dict()
        if copy_from:
            self.balances = copy_from.balances.copy()
        else:
            self._gen_accounts.add_observer(middleware.watch_gen_accounts, identify_observed=True)
            self._gen_accounts(num_accounts)
        self.initial_supply = self.supply

    @event
    def _gen_accounts(self, num):
        for i in range(num):
            k = hexhash(i)
            v = random.randint(1, 100)
            self.balances[k] = v

    @property
    def supply(self):
        return sum(self.balances.values())

    def median(self):
        return sorted(self.balances.values())[len(self.balances) / 2]

    @event
    def transfer(self, sender, receiver, amount):
        self.balances[sender] -= amount
        self.balances[receiver] += amount
        assert self.supply == self.initial_supply

    def random_transfer(self):
        "generates a valid random transfer"
        while True:
            sender = random.choice(self.balances.keys())
            if not self.balances[sender]:
                continue
            receiver = random.choice(self.balances.keys())
            if sender == receiver:
                continue
            amount = random.randint(1, self.balances[sender])
            self.transfer.add_observer(middleware.Event_transfer, identify_observed=True)
            transactionhash = hexhash(Accounts.idTransaction)

            self.transfer(sender, receiver, amount)
            Accounts.idTransaction = Accounts.idTransaction + 1
            return TransferEvent(transactionhash, sender, receiver, amount)


class Block(object):
    def __init__(self, prevblock=None, num_accounts=0):
        if not prevblock:  # genesis block
            self.accounts = Accounts(num_accounts=num_accounts)
            self.prevhash = hexhash(-1)
            self.number = 0
        else:
            self.accounts = Accounts(copy_from=prevblock.accounts)
            self.number = prevblock.number + 1
            self.prevhash = prevblock.hash
        self.transfers = []
        self.prevblock = prevblock

    def copy_transfers(self, other, fraction=0.5):
        assert isinstance(other, Block)
        for t in other.transfers[:int(len(other.transfers) * fraction)]:
            self.transfers.append(t)
            self.accounts.transfer(t.sender, t.receiver, t.amount)

    @property
    def hash(self):
        return hexhash(repr(self.__dict__))

    @event
    def random_transfers(self, num):
        for i in range(num):
            self.transfers.append(self.accounts.random_transfer())

    def serialize(self, include_balances=False):
        s = dict(number=self.number,
                 hash=self.hash,
                 prevhash=self.prevhash,
                 transfers=[dict(x._asdict()) for x in self.transfers]
                 )
        if include_balances or self.number == 0:
            s['balances'] = self.accounts.balances
        return s




def gen_chain(height, p_revert, num_accounts, max_transfers):
    head = Block(num_accounts=num_accounts)
    chain = [head]
    while head.number < height:
        if head.number > 0 and random.random() < p_revert:
            head = head.prevblock
        else:
            head = Block(prevblock=head)
            # check if there is a sibling (same block height)
            if len(chain) > 2 and chain[-2].number == head.number:
                sibling = chain[-2]
                # include some of its txs
                head.copy_transfers(sibling, 0.5)

                head.random_transfers(random.randint(0, max_transfers / 2))
            else:
                head.random_transfers(random.randint(0, max_transfers))
            chain.append(head)
    return chain


def longest_revert(chain):
    heighest = 0
    longest = 0
    for block in chain:
        heighest = max(heighest, block.number)
        longest = max(longest, heighest - block.number)
    return longest


