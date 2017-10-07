#!/usr/bin/env python3

'''
Program:     PE-P7_VSX.py
Author:      vsx-gh (https://github.com/vsx-gh)
Created:     20171004

Project Euler Problem 7:
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
    that the 6th prime is 13.

    What is the 10001st prime number?

'''

import argparse
import math

def test_prime(candidate):
    """ Tests if candidate is a prime number """
    candidate_sqrt = int(math.sqrt(candidate))
    range_end = 2

    # There is no "range" to test
    if candidate_sqrt < range_end:
        return True 

    for div in range(range_end, candidate_sqrt + 1):
        if div == candidate_sqrt:
            if candidate % div == 0:
                return False 
        elif candidate % div == 0:    # Another factor involved
            return False 
 
    return True     # Passed all disqualification tests



# Get some args
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nthprime',
                    required=True,
                    type=int,
                    help='Nth prime to find'
                    )
all_args = parser.parse_args()

prime_counter = 0
prime_candidate = 2     # First prime; avoid looping 1
curr_prime = 0
max_primes = all_args.nthprime

while prime_counter < max_primes:
    if test_prime(prime_candidate):
        prime_counter += 1
        curr_prime = prime_candidate 
        
    prime_candidate += 1

print('Prime number {} is {}'.format(max_primes, curr_prime))

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
