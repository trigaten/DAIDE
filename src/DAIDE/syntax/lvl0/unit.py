__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"

import re
from DAIDE.core import DaideObject
from DAIDE.utils.parsing import consume 
from DAIDE.utils.exceptions import ParseError 

class Unit(DaideObject):
    regex = re.compile("^[A-Za-z]{3}\s[A-Za-z]{3}\s[A-Za-z]{3}")
    
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return f"{self.string}"

    @classmethod
    def parse(cls, string, parens=False):
        """Parse UNIT or (UNIT)"""
        if parens:
            string = consume(string, "(")

        match = cls.regex.match(string)
        if match:
            matched_string = match.group()
            unit = Unit(matched_string)
            rest = string[len(matched_string):]

            if parens:
                rest = consume(rest, ")")

            return unit, rest
        else:
            raise ParseError(string, "UNIT")