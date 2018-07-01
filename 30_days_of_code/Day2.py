#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    return int(round(float(meal_cost * tip_percent / 100.0) + float(meal_cost * tax_percent / 100.0) + (meal_cost)))



if __name__ == '__main__':
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())

    print('The total meal cost is', solve(meal_cost, tip_percent, tax_percent),'dollars.')


