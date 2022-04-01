__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"

import DAIDE.syntax.lvl0.response as response
from DAIDE.syntax.lvl20.xdo import XDO
from DAIDE.syntax.lvl30.binop import BINOP

from DAIDE.syntax.daide_object import DAIDE_OBJECT
from DAIDE.utils.parsing import consume
from DAIDE.syntax.lvl0.order import ORDER 

class ARRANGEMENT(DAIDE_OBJECT):
    """an ARRANGEMENT object"""
    
    def __init__(self, arrangement):
        self.arrangement = arrangement
    
    def __str__(self):
        return str(self.arrangement)

    @classmethod
    def parse(cls, string):
        subclasses = response.RESPONSE.__subclasses__() + BINOP.__subclasses__() + [XDO]
        for subclass in subclasses:
            if consume(string, subclass.__name__, False) != False:
                arrangement, rest = subclass.parse(string)
                break
        else:
            arrangement, rest = ORDER.parse(string)

        return ARRANGEMENT(arrangement), rest

if __name__ == "__main__":
    print("HI")