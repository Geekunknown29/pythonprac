"""
QUESTION :-
Task Given an integer, n, perform the following conditional actions:

If n is odd, print Weird.
If n is even and in the inclusive range of 2 to 5, print Not Weird.
If n is even and in the inclusive range of 6 to 20, print Weird.
If n is even and greater than 20, print Not Weird.
Input Format A single line containing a positive integer, n.

Constraints 1 ≤ n ≤ 100

Output Format Print Weird if the number is weird. Otherwise, print Not Weird.

This task outlines conditions for classifying an integer as Weird or Not Weird based o
"""
#!/bin/python3

import math
import os
import random
import re
import sys


__name__ = 'sam'
if __name__ == 'sam':
    n = int(input(" give a value to variable n : "))

    assert n> 1 and n < 101, "n can not be less than 2, not even 1 and n can not be greater than 100"
        
    if n % 2  == 1 and n > 1 :
        print ("Weird")
                                
    elif n % 2 == 0 :
        if  2<=n<=5:
            print ("Not Weird")
        elif 6<=n<=20:
            print ("Weird")
        elif 21<=n<=100:
            print ("Not Weird")
