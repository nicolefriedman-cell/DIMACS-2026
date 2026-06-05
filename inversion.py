# inversion.py
# Purpose: Computes the inversion vector of a given center and permutation
# Author: Nicole Friedman
# Date: May 29, 2026

import sys

# Pre-define a center
center = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(center)

# Collect permutation from the user
permutation = input("Please enter a permutation: ").split()
errorCode = "Error: please enter a permutation of length " + str(n)
if len(permutation) != n: sys.exit(errorCode)

numInversions = 0
inversionTable = [0] * n

for i in permutation:
        i_int = int(i)
        # Compare element to all preceding elements to identify inversions
        for j_idx in range(permutation.index(i)):
                j = int(permutation[j_idx])
                if i_int in center:
                        idx = center.index(i_int)
                else:
                        sys.exit("Error: permutation value not in center")
                
                if idx < center.index(j): # Count respective inversions
                        inversionTable[idx] += 1
                        numInversions += 1

print(inversionTable)
print("Inversions:", numInversions)
