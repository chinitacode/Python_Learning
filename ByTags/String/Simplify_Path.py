'''
71. 简化路径 [中等]
以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径。

在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）；
两者都可以是复杂相对路径的组成部分。更多信息请参阅：Linux / Unix中的绝对路径 vs 相对路径

请注意，返回的规范路径必须始终以斜杠 / 开头，并且两个目录名之间必须只有一个斜杠 /。
最后一个目录名（如果存在）不能以 / 结尾。此外，规范路径必须是表示绝对路径的最短字符串。

示例 1：

输入："/home/"
输出："/home"
解释：注意，最后一个目录名后面没有斜杠。

示例 2：

输入："/../"
输出："/"
解释：从根目录向上一级是不可行的，因为根是你可以到达的最高级。

示例 3：

输入："/home//foo/"
输出："/home/foo"
解释：在规范路径中，多个连续斜杠需要用一个斜杠替换。

示例 4：

输入："/a/./b/../../c/"
输出："/c"

示例 5：

输入："/a/../../b/../c//.//"
输出："/c"

示例 6：

输入："/a//b////c/d//././/.."
输出："/a/b/c"


[注意]：
还需注意一些特殊cases如"/..." ==> "/..." 因为在Unix系统里"..."也是有效文件夹名，
和"/..hidden" ==> "/..hidden"

[Method 1]: Recursion + dfs
'''
class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path or path[0] != "/": return
        self.res = []
        self.dfs(path)
        return "".join(self.res) if self.res else "/"

    def dfs(self, path):
        if not path or path == "/": return
        tmp = "/"
        for i in range(1, len(path)):
            if path[i] == "/":
                if len(tmp) > 1:
                    self.res.append(tmp)
                self.dfs(path[i:])
                return
            if path[i] == "." and tmp[-1] != '.' and (i+1 == len(path) or path[i+1] == '/'): continue
            if i+1 < len(path) and path[i] == path[i+1] == "." and tmp[-1] != '.' and (i+2 == len(path) or path[i+2] == '/'):
                if self.res:
                    self.res.pop()
                self.dfs(path[i+2:])
                return
            tmp += path[i]
        # 处理结尾的部分
        if len(tmp) > 1:
            self.res.append(tmp)


'''
[Method 2]: 迭代+split
[Time]: O(N)
[Space]: O(N)
'''
class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path or path[0] != "/": return
        self.res = []
        for part in path.split('/'):
            if part in ('', '.'):
                pass
            elif part == "..":
                if self.res:
                    self.res.pop()
            else:
                self.res.append(part)
        return "/" + "/".join(self.res)
