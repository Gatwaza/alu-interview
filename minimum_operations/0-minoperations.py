#!/usr/bin/python3

"""
This module greedy algorithm allows pasting of contents 
exceeding target number
"""

def minOperations(n: int) -> int:
    operations = 0 
    while n > 0:
        operations += 1
        if (n & (n - 1)) == 0:
            n >>= 1
        else:
            n -= 1
    return operations
