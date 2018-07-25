#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    print(len(str(max(bin(n)[2:].split('0')))))
    # binary로 변환 => 0b00001 01 이후 문자남김 => 0을 기준으로 나눔 =>
    # 가장 큰 숫자를 구함 => 문자열로 변환 => 문자열의 길이 출력
