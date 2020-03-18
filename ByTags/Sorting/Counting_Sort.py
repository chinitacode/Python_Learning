'''
计数排序是一个非基于比较的排序算法，该算法于1954年由 Harold H. Seward 提出。
它的优势在于在对一定范围内的整数排序时，它的复杂度为Ο(n+k)（其中k是整数的范围），快于任何比较排序算法。

当然这是一种牺牲空间换取时间的做法，而且当O(k)>O(n*log(n))的时候其效率反而不如基于比较的排序
（基于比较的排序的时间复杂度在理论上的下限是O(n*log(n)), 如归并排序，堆排序）

计数排序对输入的数据有附加的限制条件：
1、输入的线性表的元素属于有限偏序集S；
2、设输入的线性表的长度为n，|S|=k（表示集合S中元素的总数目为k），则k=O(n)。
在这两个条件下，计数排序的复杂性为O(n)。
计数排序的基本思想是对于给定的输入序列中的每一个元素x，确定该序列中值小于x的元素的个数
（此处并非比较各元素的大小，而是通过对元素值的计数和计数值的累加来确定）。
一旦有了这个信息，就可以将x直接存放到最终的输出序列的正确位置上。
例如，如果输入序列中只有17个元素的值小于x的值，则x可以直接存放在输出序列的第18个位置上。
当然，如果有多个元素具有相同的值时，我们不能将这些元素放在输出序列的同一个位置上，因此，上述方案还要作适当的修改。

'''
def countingSort(arr):  # the elements in the array are all integers
    maximum, minimum = max(arr), min(arr)
    countArr = [0] * (maximum - minimum + 1)

    # record the number of times of every element in the array
    for i in arr:
        countArr[i - minimum] += 1

    # calculate the position of every element
    for i in range(1, len(countArr)):
        countArr[i] += countArr[i-1]

    targetArr = [None] * len(arr)
    for i in range(len(arr)-1, -1, -1): # reverse-order traversal is for the stability
        countIndex = arr[i] - minimum  # arr[i]在countArr里的位置
        targetArr[countArr[countIndex] - 1] = arr[i] # countArr[countIndex]是arr[i]的计数，减去1为在arr里的正确位置
        countArr[countIndex] -= 1  # 然后将其计数减一
    return targetArr

'''
第一个循环用于在额外空间中记录每一个元素出现的次数，复杂度为 O(n)；
第二个循环用于计算每一个元素的最终位置，复杂度为 O(k)， k为申请的额外空间大小；
第三个循环用于移动待排序集合中元素到已排序集合的正确位置上，复杂度为 O(n)。

由算法示例可知，计数排序的时间复杂度为 O(n+k)。
因为算法过程中需要申请一个额外空间和一个与待排序集合大小相同的已排序空间，所以空间复杂度为 O(n+k)。
由此可知，计数排序只适用于元素值较为集中的情况，若集合中存在最大最小元素值相差甚远的情况，
则计数排序开销较大、性能较差。通过额外空间的作用方式可知，
额外空间存储元素信息是通过计算元素与最小元素值的差值作为下标来完成的，
若待排序集合中存在元素值为浮点数形式或其他形式，则需要对元素值或元素差值做变换，以保证所有差值都为一个非负整数形式。

'''
