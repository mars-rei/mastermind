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

    @classmethod    
    def prompt_code(cls : Type[Code], prmpt : str) -> Code:
        while True:
            try:
                code: Code = Code(int(input(prmpt)))
                return code
            except ValueError as ex:
                print(ex)
                
print(Code.prompt_code(code_peg_choices))
