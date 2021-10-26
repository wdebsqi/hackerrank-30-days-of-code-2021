#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = -64
    for i in range(4):
        for j in range(4):
            hourglass_top = arr[i][j:j+3]
            hourglass_middle = arr[i+1][j+1]
            hourglass_bottom = arr[i+2][j:j+3]
            hourglass_summed = sum(hourglass_top) + hourglass_middle + sum(hourglass_bottom)
            if hourglass_summed > result:
                result = hourglass_summed
                
    print(result)