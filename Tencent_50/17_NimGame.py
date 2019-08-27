'''
292. Nim Game

You are playing the following Nim Game with your friend:
There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones.
The one who removes the last stone will be the winner.
You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game.
Write a function to determine whether you can win the game given the number of stones in the heap.
'''

'''
[Theorem]
The first one who got the number that is multiple of 4 (i.e. n % 4 == 0) will lost,
otherwise he/she will win.
[Proof]
1.the base case: when n = 4, as suggested by the hint from the problem,
no matter which number that that first player,
the second player would always be able to pick the remaining number.

2.For 1* 4 < n < 2 * 4, (n = 5, 6, 7),
the first player can reduce the initial number into 4 accordingly,
which will leave the death number 4 to the second player.
 i.e. The numbers 5, 6, 7 are winning numbers for any player who got it first.

3.Now to the beginning of the next cycle, n = 8,
no matter which number that the first player picks,
it would always leave the winning numbers (5, 6, 7) to the second player.
Therefore, 8 % 4 == 0, again is a death number.

4.Following the second case, for numbers between (2*4 = 8)and (3*4=12),
which are 9, 10, 11, are winning numbers for the first player again,
because the first player can always reduce the number into the death number 8.

Runtime: 4 ms, faster than 99.77% of Python online submissions for Nim Game.
Memory Usage: 11.5 MB, less than 100.00% of Python online submissions for Nim Game.
'''
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n%4
# Or(slower)
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return not n%4 == 0

'''
Method2(TLE): Recursion + memoization by hash map
'''
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        self.dic = {1: True, 2: True, 3: True, 4: False}
        def helper(n):
            if n in self.dic:
                return self.dic[n]
            else:
                self.dic[n] = not helper(n-1) and helper(n-2) and helper(n-3)
            return self.dic[n]
        return helper(n)

#Or
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res = [0, True, True, True, False]
        if n < 5:
            return res[n]
        res += [0] * (n-4)
        def helper(n):
            if res[n] != 0:
                return res[n]
            for i in range(5, n+1):
                res[i] = not (helper(i-1) and helper(i-2) and helper(i-3))
            return res[n]
        return helper(n)

'''
#or Just maintain the last three outcomes. Though TLE, but the best solution:
Finished
Runtime: 2108 ms
Your input
10009099
Output
true
Expected
true
'''
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 3:
            return True
        win = [True]*3
        i = 4
        while i <= n:
            next_outcome = (not win[0]) or (not win[1]) or (not win[2])
            win[0] = win[1]
            win[1] = win[2]
            win[2] = next_outcome
            i = i + 1
        return win[-1]
