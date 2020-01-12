import ctypes

class DynamicArray:
    def __init__(self):
        'Create an empty array.'
        self._n = 0 #size
        self._capacity = 10
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def is_empty(self):
        return self._n == 0

    # O(1)
    def __getitem__(self,k):
        if not 0 <= k < self._n:
            raise ValueError('invalid index')
        return self._A[k]

    # O(1)
    def append(self,obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _make_array(self,c):
        return (c * ctypes.py_object)()

    def _resize(self,c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    # O(n)
    def insert(self,k,value):
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
                for j in range(k,self._n - 1):
                    self._A[k] = self._A[k + 1]
                    self._A[self._n - 1] = None
                    self._n -= 1
                    return
        raise ValueError('Value not found')

    def __str__(self):
        pre = '['
        suff = ']'
        s = [str(self._A[i]) for i in range(self._n)]
        return pre + ','.join(s) + suff

    __repr__ = __str__
        
