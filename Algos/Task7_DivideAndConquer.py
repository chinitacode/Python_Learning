'''
【分治】

1.利用分治算法求一组数据的逆序对个数
2.53. Maximum Subarray [Easy]


1.求一组数据的逆序对个数
[思路]
利用merge sort的解法，讲数组分为左右两部分，
分别进行排序和merge，在merge过程中就能得到逆序对数
O(nlgn)
'''
def count_inversions(arr):
    if len(arr) <= 1: return arr, 0
    mid = len(arr) // 2
    #分别对左右进行排序并且数出逆序对
    A, X = count_inversions(arr[:mid])
    B, Y = count_inversions(arr[mid:])
    #逆序对是在对左右排好序的部分merge的过程中发现的
    def sort_and_countSplitInv(arr1, arr2):
        C = [0] * (len(arr1) + len(arr2))
        i = j = k = count = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                C[k] = arr1[i]
                i += 1
            else:
                #如果当前右边数小于左边当前的数，则把左边还剩下的数个数加入count
                #因为是排好序的，所以当右边当前数小于左边当前数，也一定小于左边剩下的数，
                #则为右边当前数与左边的数能组成的逆序对
                C[k] = arr2[j]
                count += len(arr1) - i
                j += 1
            k += 1
        #把左右部分剩下的数加入最终的数列排好
        while i < len(B):
            D[k] = B[i]
            k += 1
            i += 1
        while j < len(C):
            D[k] = C[j]
            k += 1
            j += 1
        return D,count
    D,Z = sort_and_countSplitInv(A, B)
    #返回排好序的arr和逆序对数
    return D, X+Y+Z


'''
2.
53. Maximum Subarray [Easy]
1) Divide the given array in two halves
2) Return the maximum of following three
….a) Maximum subarray sum in left half (Make a recursive call)
….b) Maximum subarray sum in right half (Make a recursive call)
….c) Maximum subarray sum such that the subarray crosses the midpoint

The lines 2.a and 2.b are simple recursive calls.
How to find maximum subarray sum such that the subarray crosses the midpoint?
We can easily find the crossing sum in linear time.
The idea is simple, find the maximum sum starting from mid point and ending at some point on left of mid,
then find the maximum sum starting from mid + 1 and ending with sum point on right of mid + 1.
Finally, combine the two and return.

Time: O(nlgn)
maxSubArraySum() is a recursive method and time complexity can be expressed as following recurrence relation.
T(n) = 2T(n/2) + Θ(n)
The above recurrence is similar to Merge Sort and can be solved either using Recurrence Tree method or Master method.
It falls in case II of Master Method and solution of the recurrence is Θ(nLogn).

Runtime: 176 ms, faster than 5.22% of Python3 online submissions for Maximum Subarray.
Memory Usage: 14.4 MB, less than 5.69% of Python3 online submissions for Maximum Subarray.
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return
        r = len(nums) - 1
        return self.maxSubArraySum(nums, 0, r)

    def maxCrossingSum(self, nums, l, mid, r):
        left_sum = float('-infinity')
        cur_sum = 0
        for i in range(mid, l-1, -1):
            cur_sum += nums[i]
            left_sum = max(left_sum,cur_sum)

        right_sum = float('-infinity')
        cur_sum = 0
        for j in range(mid+1, r+1):
            cur_sum += nums[j]
            right_sum = max(right_sum,cur_sum)

        return left_sum + right_sum

    def maxSubArraySum(self, nums, l, r):
        if l == r:
            return nums[l]
        mid = l + (r - l)//2
        return max(self.maxSubArraySum(nums, l, mid),self.maxSubArraySum(nums, mid+1, r),self.maxCrossingSum(nums,l,mid,r))
