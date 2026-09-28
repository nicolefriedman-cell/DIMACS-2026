# DIMACS-2026
Implementations of Mallows-Model related algorithms and generally practicing with Python

Definitions drawn from the 2025 paper Generalized Top-k Mallows Model for Ranked Choices by Shahrzad Haddadan, Sara Ahmadian

Note: First time using Python and code is not optimized for efficiency or modularity

Files:
- inversion.py: given a (hard coded) center and (user inputted) permutation, computes the number of inversions between the two and constructs the inversion vector
- permutation.py: given a center and inversion vector, reconstructs the permutation
- inversionHelpers.py: supplies helpers to compute inversion vectors and partition a list into a list and set at position k
- topKinversion.py: includes the i/o to collect user input about permutation size and permutation and returns inversion vectors (tested)
- TopKGMM.py: potential implementation that computes the proportional probability of a permutation under TopK General Mallows Model (not enough test cases)
