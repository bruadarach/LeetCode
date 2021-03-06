'''
A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
Also, a self-dividing number is not allowed to contain the digit zero.
Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Note:

The boundaries of each input argument are 1 <= left <= right <= 10000.
'''


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        result = []
        for i in range(left, right+1):
            if i > 0 and i < 10:
                result.append(i)
            elif i >= 10:
                for j in str(i):
                    if int(j) == 0 or i % int(j) != 0:
                        break
                else:
                    result.append(i)
        return result

# (runtime / memory)
#  44 ms / 14.3 MB
