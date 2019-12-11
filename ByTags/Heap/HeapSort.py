'''
原地堆排序
基于堆相关的操作，我们可以很容易的定义堆排序。例如，假设我们已经读入一系列数据并创建了一个堆，
一个最直观的算法就是反复的调用del_max()函数，因为该函数总是能够返回堆中最大的值，
然后把它从堆中删除，从而对这一系列返回值的输出就得到了该序列的降序排列。

真正的原地堆排序使用了另外一个小技巧。
堆排序的过程是：
创建一个堆 H[0..n-1]}
把堆首（最大值）和堆尾互换
把堆的尺寸缩小1，并调用shift_down(0),目的是把新的数组顶端数据调整到相应位置
重复步骤2，直到堆的尺寸为1

堆排序的平均时间复杂度为O(nlogn)，空间复杂度为O(1)。
'''

def heap_sort(lst):
    def sift_down(start, end):
        """最大堆调整,把小的元素往下换"""
        #其实就是把root和两个（如果有的话）孩子比大小，把最大值换到root上去，然后递归往下继续比较
        root = start
        while True:
            #左孩子
            child = 2 * root + 1
            if child > end:
                break
            #如果右孩子存在并且值大于左孩子，则让child为右孩子
            if child + 1 <= end and lst[child] < lst[child + 1]:
                child += 1

            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                break

# 创建最大堆      (len(lst) - 2)//2是最后一个元素的父元素所在index
    #从最末一个父节点往前查，维持最大堆的特性
    for start in range((len(lst) - 2)//2, -1, -1):
        sift_down(start, len(lst) - 1)

# 堆排序
    for end in range(len(lst) - 1, 0, -1):
        #把lst首的最大元素换到最末去固定好
        lst[0], lst[end] = lst[end], lst[0]
        #保持最大堆的特性的同时将lst的index往前缩小1位
        sift_down(0, end - 1)
    return lst



if __name__ == "__main__":
    l = [9, 2, 1, 7, 6, 8, 5, 3, 4]
    heap_sort(l)
    print(l)
