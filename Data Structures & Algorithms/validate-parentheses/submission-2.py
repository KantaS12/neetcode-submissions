# Dependencies
from collections import defaultdict

class Solution: 
    def isValid(self, s: str) -> bool:

        # Initialization
        stack = []
        closeToOpen = defaultdict(str)

        # Define Corresponding brackets
        closeToOpen["]"] = "["
        closeToOpen[")"] = "("
        closeToOpen["}"] = "{"

        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False
        

        