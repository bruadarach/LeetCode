'''
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

 
Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:

Input: arr = [1,2]
Output: false

Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
'''

import collections

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        arr = collections.Counter(arr)
        return sorted(list(set(arr.values()))) == sorted(list(arr.values()))

# (runtime / memory)
#  36 ms / 14.5 MB



'''
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        return len(Counter(arr)) == len(set(Counter(arr).values()))
'''
# (runtime / memory)
#  32 ms / 14.4 MB



'''
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        dict = {}
        
        for i in arr:
            if i in dict:
                dict[i] +=1
            else:
                dict[i] = 1
        
        if len(set(dict.values())) == len(dict):
            return True
        else:
            return False
'''
# (runtime / memory)
#  36 ms / 14.5 MB
