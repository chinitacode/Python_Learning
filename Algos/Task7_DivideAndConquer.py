'''
【分治】
利用分治算法求一组数据的逆序对个数
[思路]利用merge sort的解法

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
