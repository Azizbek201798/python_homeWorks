# CodeWars_Medium_1 => Azizbek

# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

import os
os.system("clear")

def max_sequence(arr):
    max_sum = 0
    summa = 0

    for i in arr:
        summa += i
        max_sum = max(max_sum,summa)
        if summa < 0:
            summa = 0
    
    return max_sum
