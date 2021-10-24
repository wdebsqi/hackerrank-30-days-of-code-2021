#!/bin/python3

import math
import os
import random
import re
import sys

def base_10_to_base_2(base_10_num):
    result = 0
    i = 0
    r = 0
    while (base_10_num):
        base_10_num, r = divmod(base_10_num, 2)
        result += 10**i * r
        i += 1
        
    return str(result)


if __name__ == '__main__':
    n = int(input().strip())
    
    n_to_base_2 = base_10_to_base_2(n)
    n_to_base_2_splitted = n_to_base_2.split('0')
    result = len(max(n_to_base_2_splitted, key=len))
    print(result)
