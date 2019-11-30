# in-place
def merge_sort(arr):
    if len(arr) <= 1: return
    # list slicing making new copies of arr, using extra space
    l, r = arr[:len(arr)//2], arr[len(arr)//2:]
    merge_sort(l)
    merge_sort(r)
    # merging process
    i = j = k = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1

    # complet filling arr, 因为最后总会剩下l或者r的元素（最大的几个元素）
    while i < len(l):
        arr[k] = l[i]
        i += 1
        k += 1
    while j < len(r):
        arr[k] = r[j]
        j += 1
        k += 1

if __name__ == '__main__':
    random_list_of_nums = [5, 8, 10, 8, 9, 10, 8]
    print('Before: ',random_list_of_nums)
    merge_sort(random_list_of_nums)
    print('After: ',random_list_of_nums)
    random_list_of_nums = [4,4,2,4,5,6,1,9,4]
    print('Before: ',random_list_of_nums)
    merge_sort(random_list_of_nums)
    print('After: ',random_list_of_nums)
