"""Suppose you are given an array of ints, for example A[ ] = {1, - 1, 3, 8 ,4 }
Maximize the sum of array elements such that if you include a number in the sum, you may 
not use adjacent numbers in the sum. So in the example above the max sum is 1 + 8 = 9 
In A[ ] = { 1, 5, 3, 9, 4 } the max sum is 5 + 9 = 14. 
and in A[ ] = { 1,2,3,4, 5} max sum is 1 + 3 + 5 = 9"""

from __future__ import print_function
import sys

def set_value(iArr, idx):
    if idx < len(iArr):
        return max(iArr[idx],0)
    else:
        return 0    

def max_non_adj_sum(iArr):
    "calcuate the maximum sum of non adjacent elements"
    arr_len = len(iArr)
    cur_sum = 0
    i = 0
    while i < arr_len:

        # if at the end of the array we don't have a choice
        if i == (arr_len-1):
            if iArr[i] > 0:
                cur_sum += iArr[i]
                return cur_sum

        # choose between adding iArr[i] or iArr[i+1] to the sum
        # if elements are negative or out of bounds
        # set their values to zero for the calculation
        a0 = set_value(iArr, i)
        a1 = set_value(iArr, i+1)
        a2 = set_value(iArr, i+2)
        a3 = set_value(iArr, i+3)
        a4 = set_value(iArr, i+4)

        # for iArr[i]
        sum0 = max((a0+a2+a4),(a0+a3))
        # for iArr[i+1] 
        sum1 = max((a1+a3),(a1+a4))

        # choose based on greater of two max sums
        if sum0 >= sum1:
            if iArr[i] > 0:
                cur_sum += iArr[i]
            i += 2
        else:
            if iArr[i+1] > 0:
                cur_sum += iArr[i+1]
            i += 3            

    return cur_sum
            

# main program
num_inputs=int(sys.stdin.readline())

# reading each input at a time
for in_num in range(num_inputs):
    arr_str = sys.stdin.readline()
    in_arr = [int(x) for x in arr_str.split()]
    max_sum = max_non_adj_sum(in_arr)
    print(max_sum)

