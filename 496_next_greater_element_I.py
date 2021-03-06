'''
You are given two integer arrays nums1 and nums2 both of unique elements, where nums1 is a subset of nums2.
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, return -1 for this number.


Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation:
For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
For number 1 in the first array, the next greater number for it in the second array is 3.
For number 2 in the first array, there is no next greater number for it in the second array, so output -1.


Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation:
For number 2 in the first array, the next greater number for it in the second array is 3.
For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
 

Constraints:

1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 10^4
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.
 

Follow up: Could you find an O(nums1.length + nums2.length) solution?
'''


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        result = []
        for i in nums1:
            idx = nums2.index(i)
            for j in range(idx, len(nums2)):
                if nums2[j] > i:
                    result.append(nums2[j])
                    break
            else:
                result.append(-1)
        return result

# (runtime / memory)
#  64 ms / 14.3 MB


'''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums2_idx = {num:idx for idx, num in enumerate(nums2)}
        
        for i in nums1:
            idx = nums2_idx[i]
            
            for j in nums2[idx:]:
                if j > i:
                    result.append(j)
                    break
            else:
                result.append(-1)
        return result 
'''
# (runtime / memory)
#  52 ms / 14.7 MB



##### STACK! #####
''' 
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if not nums1 or not nums2:
            return []
        
        mapper = {}
        stack = [nums2[0]]
        
        for i in range(1,len(nums2)):
            while stack and nums2[i] > stack[-1]:
                mapper[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        for key in stack:
            mapper[key] = -1
        return [mapper[i] for i in nums1]
'''
# (runtime / memory)
#  40 ms / 14.6 MB
