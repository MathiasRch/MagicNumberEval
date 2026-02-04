import random
from common.imodel import IModel


class Model(IModel):

    def __init__(self):
        self._magic_number = random.randint(0, 100)
        self._proposal_count = 0
        self._max_proposals = 10

    def compareToMagicNumber(self, num: int) -> int:
        self._proposal_count += 1

        if num == self._magic_number:
            return 0
        elif num < self._magic_number:
            return -1
        else:
            return 1

    def getProposalCount(self) -> int:
        return self._proposal_count

    def getMaxNumberOfProposals(self) -> int:
        return self._max_proposals
