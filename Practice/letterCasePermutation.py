#Using Divide and Conquer:

def letterCasePermutation(S, rule):
    rule = rule.lower()
    rule = rule + rule.upper()
    def helper(S, rule):
        if len(S) == 1:
            tmp = S[0]
            if tmp not in rule:
                return [S]
            else:
                if tmp == tmp.upper():
                    return [S, tmp.lower()]
                else:
                    return [S, tmp.upper()]
        mid = len(S)//2
        left = helper(S[:mid], rule)
        right = helper(S[mid:], rule)
        return [x + y for x in left for y in right]
    return helper(S, rule)
