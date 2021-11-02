#!/bin/python3

import math
import os
import random
import re
import sys


S = input()

try:
    converted = int(S)
    print(converted)
except ValueError:
    print('Bad String')