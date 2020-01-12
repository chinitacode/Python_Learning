class li:
    def __init__(self,*args):
        self.data = [e for e in args]
        print(self.data)

    def __len__(self):
        len = 0
        for e in self.data:
            len += 1
        return len

    def is_empty(self):
        return len(self.data) == 0

    def __getitem__(self,k):
        if not 0 <= k < len(self.data):
            raise ValueError('invalid index')
        return self.data[k]

    def __str__(self):
        pre = '['
        suff = ']'
        s = [str(e) for e in self.data]
        return pre + ','.join(s) + suff

    __repr__ = __str__
