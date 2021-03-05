'''
You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule.

 

Example 1:

Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
Output: 1
Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].

Example 2:

Input: items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"
Output: 2
Explanation: There are only two items matching the given rule, which are ["phone","blue","pixel"] and ["phone","gold","iphone"]. Note that the item ["computer","silver","phone"] does not match.
 

Constraints:

1 <= items.length <= 104
1 <= typei.length, colori.length, namei.length, ruleValue.length <= 10
ruleKey is equal to either "type", "color", or "name".
All strings consist only of lowercase letters.
'''



class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:

        count = 0
        for i in range(len(items)):
            if ruleKey == "type" and items[i][0] == ruleValue:
                count += 1
            elif ruleKey == "color" and items[i][1] == ruleValue:
                count += 1
            elif ruleKey == "name" and items[i][2] == ruleValue:
                count += 1
        return count

# (runtime / memory)
#  232 ms / 20.4 MB



'''
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        count = 0
        for i in range(len(items)):
            if ruleValue in items[i]:
                if ruleKey == "type" and items[i][0] == ruleValue:
                    count += 1
                elif ruleKey == "color" and items[i][1] == ruleValue:
                    count += 1
                elif ruleKey == "name" and items[i][2] == ruleValue:
                    count += 1
        return count
'''
# (runtime / memory)
#  224 ms / 20.6 MB



'''
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        dic = {'type':0, 'color':1, 'name':2}
        count = 0
        
        for i in items:
            if i[dic[ruleKey]] == ruleValue:
                count += 1
        return count
'''
# (runtime / memory)
#  240 ms / 20.6 MB



'''
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        dic = {'type':0, 'color':1, 'name':2}
        return sum (1 for i in items if i[dic[ruleKey]] == ruleValue)
'''
# (runtime / memory)
#  240 ms / 20.6 MB



'''
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        count = 0
        for t,c,n in items:
            if (ruleKey, ruleValue) in (("type",t),("color",c),("name",n)):
                count += 1
        return count 
'''
# (runtime / memory)
#  232 ms / 20.6 MB



'''
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        return sum(1 for t,c,n in items if (ruleKey, ruleValue) in (("type",t),("color",c),("name",n)))
'''
# (runtime / memory)
#  252 ms / 20.6 MB
