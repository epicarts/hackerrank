#!/bin/python3

import sys


S = input().strip()
try:
    print(int(S))
    pass
except:
    print("Bad String")
