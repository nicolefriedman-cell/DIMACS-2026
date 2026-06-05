import math

# Purpose: Split a list into a list of size k and set of the remaining k+1 to n
# Arguments: the list to split and the partition point k
# Returns: a topK list and a remainder set
def partition(list, k):
        n = len(list)
        topK = []
        remainder = set()

        for i in range(k):
                topK.insert(i, list[i])
        
        for i in range(k, n):
                remainder.add(list[i])

        return topK, remainder


# Construct the disjoint set 
def constructVectors(topKcenter, permutation, k):
        l = 0
        disjoint = []
        for i in permutation:
                if i in topKcenter:
                        l += 1
                else:
                        disjoint.append(i)

        # Initialize I and P vectors, and compute Q
        I = [0] * k
        P = [0] * k
        Q = math.comb(k - l, 2)

        # Compute I and P vectors iteratively
        for i in permutation:
                # Handle the case for elements that are not topk in the center
                if i not in topKcenter:
                        # Swaps based on size of displaced, location, and offset
                        idx = permutation.index(i)
                        position = k - (idx + 1)
                        disjointSize = len(disjoint)
                        offset = disjointSize - (disjoint.index(i) + 1)
                        I[idx] = disjointSize + position - offset

                        # Construct P vector
                        for j_idx in range(permutation.index(i)+1, k):
                                j = permutation[j_idx]
                                if j not in topKcenter:
                                        P[idx] += 1
                else: # Case where elemenets were topk in the center
                        for j_idx in range(permutation.index(i) + 1, k):
                                j = permutation[j_idx]
                                idx = topKcenter.index(i)
                                # Count swaps for elements that were both topk
                                if j in topKcenter and idx > topKcenter.index(j):
                                        I[permutation.index(i)] += 1
                        for j in topKcenter:
                                # Count elements that were displaced out of top k
                                if (j not in permutation and 
                                topKcenter.index(j) < topKcenter.index(i)):
                                        I[permutation.index(i)] += 1

        return I, P, Q
