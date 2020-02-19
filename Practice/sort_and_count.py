def sort_and_count(arr):
    if len(arr) == 1:
        return arr, 0
    mid = len(arr)//2
    B, X = sort_and_count(arr[:mid])
    C, Y = sort_and_count(arr[mid:])
    def sort_and_countSplitInv(B, C):
        D = [0] * (len(B) + len(C))
        i = j = k = count = 0
        while i < len(B) and j < len(C):
            if B[i] < C[j]:
                D[k] = B[i]
                i += 1
            else:
                D[k] = C[j]
                j += 1
                count += (len(B) - i)
            k += 1
        while i < len(B):
            D[k] = B[i]
            k += 1
            i += 1
        while j < len(C):
            D[k] = C[j]
            k += 1
            j += 1
        return D,count
    D,Z = sort_and_countSplitInv(B,C)
    return D, X+Y+Z
