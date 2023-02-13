#!/usr/bin/python3

def minOperations(n: int) -> int:
    operations = 0 #counter to store n of operations
    while n > 0:
        operations += 1
        if (n & (n - 1)) == 0:
            n >>= 1 #copy and paste while function
        else:
            n -= 1
    return operations
