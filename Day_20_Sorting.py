#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    
    total_swaps = 0
    while True:
        this_iteration_swaps = 0
        
        for i in range(len(a) - 1):
            if a[i] > a[i+1]:
                tmp = a[i+1]
                a[i+1] = a[i]
                a[i] = tmp
                this_iteration_swaps += 1
        
        if this_iteration_swaps == 0:
            break
        
        total_swaps += this_iteration_swaps
        
    print(f"Array is sorted in {total_swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")