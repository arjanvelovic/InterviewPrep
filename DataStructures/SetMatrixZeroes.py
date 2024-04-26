def setZeroes(matrix):
    zero_row = []
    zero_column = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                zero_row.append(i)
                zero_column.append(j)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i in zero_row or j in zero_column:
                matrix[i][j] = 0
                
    return matrix

print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))