def knapsack(S, T):
    """
    Counter Examples
    a) Put the elements of S in the knapsack in left to right order if they fit, i.e. the first-fit algorithm.
    a) [4, 3, 2], 5 
    (b) Put the elements of S in the knapsack from smallest to largest, i.e. the best-fit algorithm.
    b) [2,3], 3
    (c) Put the elements of S in the knapsack from largest to smallest.
    c) [5,4,3] 7
    """
    return S, T

if __name__ == "__main__":
    knapsack([1,2,5,9,10], 22)