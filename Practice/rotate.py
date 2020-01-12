# in-place

def rotate_in_place(matrix):
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]  # save top
            
            ## left->top
            matrix[first][i] = matrix[last-offset][first]
            
            ##bottom -> left
            matrix[last-offset][first] = matrix[last][last - offset];

            # right -> bottom
            matrix[last][last - offset] = matrix[i][last];

            # top -> right
            matrix[i][last] = top;  # right <- saved top            
            
    for x in matrix:
        print(x, sep=" ")

        
matrix = [[i*5+j for j in range(5)] for i in range(5)]
