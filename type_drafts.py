from __future__ import annotations
from enum import Enum
from typing import Type

code_peg_choices : str = \
"""
Please select a valid coloured code peg (1-6): 
1. Orange
2. Green
3. Blue
4. Yellow
5. Purple
6. Brown
"""

class Code(Enum):
    Empty = 0
    Orange = 1
    Green = 2
    Blue = 3
    Yellow = 4
    Purple = 5
    Brown = 6

    def describe(self):
            # self is the member here
            return self.name, self.value

    @classmethod    
    def prompt_code(cls : Type[Code], prmpt : str) -> Code:
        while True:
            try:
                print(prmpt)
                code: Code = Code(int(input(">")))
            except ValueError as ex:
                print("That is an invalid code peg choice.")
                
print(Code.prompt_code((code_peg_choices))) #checks if input given is valid
print(Code.Empty.describe()) #prints out the enumerated tuple
