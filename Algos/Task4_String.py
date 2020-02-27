'''
【字符串】
实现KMP算法
实现一个字符集，只包含 a～z 这 26 个英文字母的 Trie 树
实现朴素的字符串匹配算法

【kmp算法】
'''
def kmp(string, sub_string):
    nxt = make_nxt(sub_string)
    i = j = 0
    while i < len(string) and j < len(sub_string):
        # 如果是子串开头或者刚好匹配：
        if j == -1 or string[i] == sub_string[j]:
            i += 1
            j += 1
        else: # 如果子串刚开始就不匹配，则j = nxt[0] = -1
            j = nxt[j]
    if j == len(sub_string):
        return i - j
    return -1

# return nxt数组，储存从索引0开始到当前字符组成的字符串的最大相同前后缀长度
# 如'abcd'的next为[-1,0,0,0]
def make_nxt(modestr):
    # 任何字符串的next数组前两位都为-1,0（-1表示前面没有子串，0表示没有匹配，因为第一个字符没有前后缀）
    Next = [0]*len(modestr)
    Next[0] = -1
    i = 0
    j = -1
    # while not finish whole modestr
    while i < len(modestr)-1: # 因为next表示的是当前字符前的字符串的最长前后缀，所以不需要考虑最后一个字符
        # 一开始j就为-1，所以i,j都加1使得第二个字符的next值为0，因为第二个字符之前的字符串就是第一个字符，肯定为0
        if j == -1 or modestr[i] == modestr[j]:
            # if first element of substring or match, check next
            i += 1
            j += 1
            Next[i] = j # NextArray[i]的值为之前字符串已匹配的长度
        else:
            # not match, jump to next j
            j = Next[j]
    # in the outer loop, j == -1 is a trivial condition
    return Next


if __name__ == '__main__':
    print(make_nxt('abcdabcyabc'))  # [-1, 0, 0, 0, 0, 1, 2, 3, 0, 1, 2]
    print(make_nxt('ababa'))  # [-1, 0, 0, 1, 2]
    print(make_nxt('abcdabcy')) # [-1, 0, 0, 0, 0, 1, 2, 3]
    print(make_nxt('xyxyyxxyx'))  # [-1, 0, 0, 1, 2, 0, 1, 1, 2]

    print(kmp('abcxabcdabcdabcy','abcdabcy')) # 8
    print(kmp("bacbababadababacambabacaddababacasdsd", "ababaca")) # 10
