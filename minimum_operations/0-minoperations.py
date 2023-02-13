#!/usr/bin/python3

"""

This module allows pasting of contents 
exceeding target number.

"""

def minOperations(n):
    if n <= 0:
        return 0
    result = 0
    i = 2
    while i * i <= n:
        while n % i == 0:
            result += 1
            n = n // i
        i += 1
    if n > 1:
        result += 1
    return result

