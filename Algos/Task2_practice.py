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


'''
# 32. Longest Valid Parentheses
  O(n)
Runtime: 40 ms, faster than 59.26% of Python online submissions for Longest Valid Parentheses.
Memory Usage: 12.1 MB, less than 100.00% of Python online submissions for Longest Valid Parentheses.

1. Scan the string from beginning to end by its index.
2. If current character is '(', push its index to the stack.
   If current character is ')' and the character at the index of the top of stack is '(',
   we just find a matching pair so pop from the stack and update result as the
   distance between the current index i and the index of stack[-1].
   Otherwise, we push the index of ')' to the stack.
3. After the scan is done, the stack will only
   contain the indices of characters which cannot be matched. Then
   return result.
4. If the stack is empty, the whole input
   string is valid. Otherwise, we can scan the stack to get longest
   valid substring as described in step 3.
'''
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        result = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif stack == [] or s[stack[-1]] != '(':
                stack.append(i)
            else:
                stack.pop()
                result = max(result, i - stack[-1]) if stack != [] else i + 1
        return result

'''
# Or: To make sure the stack is not empty,
      first put in a tuple (-1, ')')
      as it will never be poped out and -1 can be used to calculate result.

Runtime: 32 ms, faster than 92.42% of Python online submissions for Longest Valid Parentheses.
Memory Usage: 13.4 MB, less than 14.29% of Python online submissions for Longest Valid Parentheses.
'''
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack, result = [(-1, ')')], 0
        for i, paren in enumerate(s):
            if paren == ')' and stack[-1][1] == '(':
                stack.pop()
                result = max(result, i - stack[-1][0])
            else:
                stack += (i, paren),
        return result


'''
Or: add 0 to stack is c is '(',
    only add 2 to stack[-1], update longest when a pair of parenthesis is canceled out,
    else reset stack = [0] to avoid the length of another slice of parentheses got added to longest
'''
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]
        longest = 0

        for c in s:
            if c == "(":
                stack.append(0)
            else:
                # if stack is not really empty
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val + 2
                    longest = max(longest, stack[-1])
                else:
                    # separate slices of parentheses with distance in between
                    stack = [0]

        return longest
