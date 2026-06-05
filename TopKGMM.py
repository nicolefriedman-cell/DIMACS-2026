from inversionHelpers import constructVectors, partition
import math
import sys

center = list(range(1,101))
n = len(center)

########################### Permutation Collection ############################
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

############################# Constant Parameters #############################
#beta = input("Please enter a concentration parameter: ")
beta = 1
# p = input("Please enter a parameter p: ")
p = 1
# w = input("Please enter weights: ").split()
w = [1] * k


################################## TopKGMM ####################################
I, P, Q = constructVectors(topKcenter, permutation, k)

KendallTau = w[0] * p * Q

for i in range(k):
        KendallTau += w[i] * (I[i] + p * P[i])

probability = math.exp(-beta * KendallTau)

print("The probability of the provided permutation in the model is " \
"proportional to", probability)