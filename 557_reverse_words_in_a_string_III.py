'''
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
'''


class Solution:
    def reverseWords(self, s: str) -> str:

        s = s.split()

        result = []
        for i in s:
            result.append(i[::-1])
        return ' '.join(result)

# (runtime / memory)
#  28 ms / 14.8 MB



'''
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        for i in range(len(s)):
            s[i] = s[i][::-1]
        return " ".join(s)
'''
# (runtime / memory)
#  28 ms / 14.8 MB
