#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fizzBuzz' function below.
#
# Given a number n for each integer  i  in the range from 1 to n print one value per line
# as follows
# if i is multiple of .both 3 and 5  print FizzBuzz
# if i is a multiple of three  print Fizz 36912151821242730
# If i is a multiple of five print Buzz 5101520253035404550
#

def fizzBuzz(n):
    # Write your code here
    for i in range(1, n+1):
        three = i%3
        five = i%5
        if three == 0 and five == 0:
            print("FizzBuzz")
        elif three == 0 :
            print("Fizz")
        elif five ==0:
            print("Buzz")
        else:
            print(i)


if __name__ == '__main__':
    fizzBuzz(30)
