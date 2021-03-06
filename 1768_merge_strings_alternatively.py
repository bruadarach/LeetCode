'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.

 
Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
'''


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        new = ""

        for i in range(max(len(word1), len(word2))):  # 3 # 0,1,2
            if len(word1)-1 >= i and len(word2)-1 >= i:
                new += word1[i]
                new += word2[i]

            elif len(word1)-1 < i and len(word2)-1 >= i:
                new += ""
                new += word2[i]

            elif len(word1)-1 >= i and len(word2)-1 < i:
                new += word1[i]
                new += ""

        return new

# (runtime / memory)
#  16 ms / 14.1 MB



''' ##### zip_longest(iterable1, iterable2, fillvalue="")

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        return ''.join(i+j for i, j in zip_longest(word1,word2, fillvalue=''))
'''
# (runtime / memory)
#  28 ms / 14.2 MB



'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        new = ''
        
        for i in range(min(len(word1), len(word2))):
            new += word1[i]+word2[i]
        
        return new + word1[i+1:] + word2[i+1:]
'''
# (runtime / memory)
#  28 ms / 14.4 MB
