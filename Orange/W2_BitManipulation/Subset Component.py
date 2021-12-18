# Hackker ranks
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findConnectedComponents' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY d as parameter.
#

def count_components(val):
    s = 0
    for i in range(64):
        if val & 1 << i != 0:
            s += 1
    return s


if __name__ == '__main__':
    n = int(input().strip())
    d = input().strip().split()
    d = [int(v) for v in d]
    assert len(d) == n

    result = 0
    for k in range(64):
        mask = 1 << k
        temp = []
        for i in range(n):
            if d[i] & mask != 0:
                temp.append(d[i])

        for i in range(len(temp)):
            val = 0
            for j in range(i, len(temp)):
                val = d[i] | d[j]
                result += 64 - count_components(val) + 1
    print(result)