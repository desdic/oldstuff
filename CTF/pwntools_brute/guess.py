#!/usr/bin/env python

import random

N = random.randrange(1, 100)
A = 0

while N != A:
    A = int(input("Guess what number I'm thinking off: "))
    if N == A:
        print("flag{found_the_number}")
    else:
        print("Nope, try again")
