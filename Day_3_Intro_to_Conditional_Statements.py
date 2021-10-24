#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    string_weird = 'Weird'
    string_not_weird = 'Not Weird'
    
    if N % 2 != 0:
        print(string_weird)
    elif N >= 2 and N <= 5:
        print(string_not_weird)
    elif N >= 6 and N <= 20:
        print(string_weird)
    else:
        print(string_not_weird)
