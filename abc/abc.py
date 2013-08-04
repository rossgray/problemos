"""String Reduction 

Given a string consisting of a,b and c's, we can perform the following operation: 
Take any two adjacent distinct characters and replace it with the third character. 
For example, if 'a' and 'c' are adjacent, they can replaced with 'b'. 
What is the smallest string which can result by applying this operation repeatedly? 

Input: 
The first line contains the number of test cases T. T test cases follow. 
Each case contains the string you start with. 

Output: 
Output T lines, one for each test case containing the smallest length of the 
resultant string after applying the operations optimally. 

Constraints: 
1 <= T <= 100 
The string will have at most 100 characters. 

Sample Input: 
3 
cab 
bcab 
ccccc 

Sample Output: 
2 
1 
5 

Explanation: 
For the first case, you can either get cab -> cc or cab -> bb, resulting in a string of length 2. 

For the second case, one optimal solution is: bcab -> aab -> ac -> b. 
No more operations can be applied and the resultant string has length 1.
 
For the third case, no operations can be performed and so the answer is 5."""

from __future__ import print_function
import sys


def replace_chars(char1, char2):
    "Replaces 2 chars in the set (a, b, c) with the one missing" 
    if char1 == char2:
        print('Error: char1 and char2 should not be the same')
        return '0'
    if char1 == 'a':
        if char2 == 'b':
            return 'c'
        else:
            return 'b'
    elif char1 == 'b':
        if char2 == 'a':
            return 'c'
        else:
            return 'a'
    elif char1 == 'c':
        if char2 == 'a':
            return 'b'
        else:
            return 'a'                         


def reduce_string(cur_str, index):

    print ("cur_str = ", cur_str)
    finished = True
    while (len(cur_str) - index) > 1:
        str_len = len(cur_str) - index
        if str_len > 3:
            # just take first 4 chars of string
            sub_str = cur_str[index:index+4];
            before_str = cur_str[:index];
            if str_len > 4:
                after_str = cur_str[index+4:]
            else:
                after_str = '' 
            # we just want to try and endure that there
            # will not be 3 consecutive chars after transformation
            for i in range(3):
                char1 = sub_str[i]
                char2 = sub_str[i+1]
                if char1 != char2:
                    new_char = replace_chars(char1, char2)
                    if (new_char != sub_str[(i+2)%4]) or (new_char != sub_str[(i+3)%4]):
                        finished = False
                if not finished:
                    # create new string
                    if i == 0:
                        new_sub_str = new_char + sub_str[2:]
                    elif i == 1:
                        new_sub_str = sub_str[0] + new_char + sub_str[3]
                    else:
                        new_sub_str = sub_str[:2] + new_char
                    cur_str = before_str + new_sub_str + after_str
                    break
        if str_len == 3:
            sub_str = cur_str[index:index+3]
            before_str = cur_str[:index];
            # if all three chars are the same then we can finish
            if (sub_str[0] == sub_str[1]) and (sub_str[1] == sub_str[2]):
                return cur_str
            for i in range(2):
                char1 = sub_str[i]
                char2 = sub_str[i+1]
                if char1 != char2:
                    new_char = replace_chars(char1, char2)
                    finished = False
                if not finished:
                    # create new string
                    if i == 0:
                        new_sub_str = new_char + sub_str[2]
                    else:
                        new_sub_str = sub_str[0] + new_char  
                    cur_str = before_str + new_sub_str
                    break          

        if str_len == 2:
            sub_str = cur_str[index:index+2]
            before_str = cur_str[:index]
            # if both chars are the same then we can finish
            if sub_str[0] == sub_str[1]:
                return cur_str
            # else replace chars and finish
            new_char = replace_chars(sub_str[0], sub_str[1])
            cur_str = before_str + new_char
            return cur_str   

        if finished:
            return reduce_string(cur_str, index+1)
        else:
            return reduce_string(cur_str, index)                                    


# main program
num_inputs=int(sys.stdin.readline())

# reading each input at a time
for in_num in range(num_inputs):
    cur_str = sys.stdin.readline()
    #need to remove end of line char from end of string
    cur_str=cur_str[:-1]
    cur_str=reduce_string(cur_str, 0)
    print(len(cur_str))
