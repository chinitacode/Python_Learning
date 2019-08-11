'''
20. Valid Parentheses
'''
class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

#Or:
def isValid(s):
    stack = []
    for c in s:
        if (c == '(' or c == '[' or c == '{'):
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            if (   (c == ')' and stack[-1] == '(')
                or (c == ']' and stack[-1] == '[')
                or (c == '}' and stack[-1] == '{')):
                stack.pop()
            else:
                return False
    return len(stack) == 0
