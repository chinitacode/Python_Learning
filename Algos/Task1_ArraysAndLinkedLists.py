# 实现一个支持动态扩容的数组
'''
ADT List Operations
Create an empty list
Determine whether the list is empty
Determine the number of items in a list
Add an item at given position in a list
Remove the item at a given position in a list
Remove all the items from a list
Get the item at a given position in a list
'''

import ctypes

class DynamicArray:

    def __init__ (self):
        'Create an empty array.'
        self._n = 0 #size
        self._capacity = 10
        self._A = self._make_array(self._capacity)

    def __len__ (self):
        return self._n

    def is_empty(self):
        return self._n == 0

    # O(1)
    def __getitem__ (self, k):
        if not 0 <= k < self._n:
            raise ValueError('invalid index')
        return self._A[k]

    # O(1)
    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _make_array(self, c):
        return (c * ctypes.py_object)( )

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    # O(n)
    def insert(self, k, value):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j-1]
        self._A[k] = value
        self._n += 1

    # O(n)
    def remove(self, value):
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n - 1):
                    self._A[j] = self._A[j+1]
                self._A[self._n - 1] = None
                self._n -= 1
                return
        raise ValueError( 'value not found' )

    def merge(self, li):
        m = self._n
        n = len(li)
        for i in range(n):
            self.append(0)
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if self._A[i] > li[j]:
                self._A[k] = self._A[i]
                i -= 1
            #Duplicate numbers in nums2 are put behind numbers in nums1
            else:
                self._A[k] = li[j]
                j -= 1
            k -= 1
        #Copy the remaining value of nums2 to the left side to nums1
        if j >= 0:
            self._A[:k + 1] = li[:j + 1]


    def __repr__(self):
        return repr(self._A[:self._n])


    def __str__(self):
        return f"size: {self._n}, capacity: {len(self._A)}\n{str(self._A[:self._n])}"

mylist = DynamicArray()
li = [2, 6, 10, 28]
print ('size was: ', str(len(mylist)))
mylist.append(10)
print(mylist[0])
mylist.append(20)
mylist.append(30)
mylist.insert(0, 0)
mylist.insert(1, 5)
mylist.insert(3, 15)
print(mylist)
print(mylist.__str__())
mylist.remove(20)
print(mylist.__repr__())
print ('size is: ', str(mylist.__len__()))
mylist.merge(li)
print(mylist)


# 实现两个有序数组合并为一个有序数组 (88. Merge Sorted Array)
# Two pointers
def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i, j, k = m - 1, n - 1, m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        #Duplicate numbers in nums2 are put behind numbers in nums1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    #Copy the remaining value of nums2 to the left side to nums1
    if j >= 0:
        nums1[:k + 1] = nums2[:j + 1]
'''
Time Complexity: O(m+n) where m and n are the number of non-zero elements in nums1
and nums2 respectively, since we are iterating over both arrays in order to merge them.
Space Complexity: O(1) since we are doing the merging in place
'''
