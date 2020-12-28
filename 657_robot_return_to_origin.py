'''
There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.
The move sequence is represented by a string, and the character moves[i] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.
Note: The way that the robot is "facing" is irrelevant. "R" will always make the robot move to the right once, "L" will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.

 
Example 1:

Input: moves = "UD"
Output: true
Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.

Example 2:

Input: moves = "LL"
Output: false
Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because it is not at the origin at the end of its moves.

Example 3:

Input: moves = "RRDD"
Output: false

Example 4:

Input: moves = "LDRRLRUULR"
Output: false
 

Constraints:

1 <= moves.length <= 2 * 104
moves only contains the characters 'U', 'D', 'L' and 'R'.
'''


class Solution:
    def judgeCircle(self, moves: str) -> bool:

        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')

# (runtime / memory)
#  20 ms / 14.6 MB



'''
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        count1 = 0
        count2 = 0
        
        for i in moves:
            if i == 'U':
                count1 += 1
            elif i == 'D':
                count1 -= 1
            elif i == "L":
                count2 += 1
            elif i == "R":
                count2 -= 1
        
        if (count1 == 0) and (count2 == 0):
            return True
        else:
            return False
'''
# (runtime / memory)
#  60 ms / 14.5 MB



'''
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        position = [0,0]
        for i in moves:
            
            if i == "U":
                position[0] +=1
            elif i == "D":
                position[0] -=1
            elif i == "R":
                position[1] +=1
            elif i == "L":
                position[1] -=1
        
        return position == list([0,0])
'''
# (runtime / memory)
#  68 ms / 14.7 MB

