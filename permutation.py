# permutation.py
# Purpose: Reconstructs a permutation from a given center and inversion
# Author: Nicole Friedman
# Date: May 29, 2026

import sys

# Pre-define a center
center = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(center)

# Collect table from the user
inversionTable = input("Please enter an inversion table: ").split()
errorCode = "Error: please enter an inversion table of length " + str(n)
if len(inversionTable) != n: sys.exit(errorCode)

permutation = []

# For each table value starting from the end, reconstruct the permutation
idx = n - 1
while idx >= 0:
        permutation.insert(int(inversionTable[idx]), center[idx])
        idx -= 1

print(permutation)