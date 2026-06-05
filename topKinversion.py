# topKinversion.py
# Purpose: Computes the Inversion Vectors of a Top-k list given a center,
#          parameter k, and a permutation
# Author: Nicole Friedman
# Date: May 31, 2026

import sys
import math
from inversionHelpers import constructVectors, partition
        
# Pre-define a center
center = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(center)

# Collect rank size from the User
k = int(input("Please enter the k value: "))
errorCode = "Error: please enter a k value less than " + str(n)
if k > n: sys.exit(errorCode)

# Split center into top k and remainder based on size of k
topKcenter, remainingCenter = partition(center, k)

# Collect permutation from user; only care about top k
charPermutation = input("Please enter a permutation of length k: ").split()
if len(charPermutation) != k: sys.exit("Error: please enter a permutation of " \
                                   "length k")
permutation = [int(char) for char in charPermutation] # List of ints

# Construct the remaining k+1 to n set from elements not in permutation
remainingPerm = set()
for i in center:
        if i not in permutation: 
                remainingPerm.add(i)

I, P, Q = constructVectors(topKcenter, permutation, k)
print("I:", I)
print("P:", P)
print("Q:", int(Q))