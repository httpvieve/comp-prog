
import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    max_counter = 0
    max_candle = max(candles)
    for val in candles:
        if val == max_candle:
            max_counter += 1
    return max_counter
if __name__ == '__main__':
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))