def spiralOrder(matrix):
    spiralorder = []

    m = len(matrix) -1
    n = len(matrix[0]) - 1

    row_beg = 0
    row_end = m
    col_beg = 0
    col_end = n

    while (row_beg <= row_end and col_beg <= col_end):

        for i in range(col_beg, col_end + 1):
            spiralorder.append(matrix[row_beg][i])
        row_beg += 1
        for i in range(row_beg, row_end+1):
            spiralorder.append(matrix[i][col_end])
        col_end -= 1
        if row_beg <= row_end:
            for i in range(col_end, col_beg-1, -1):
                spiralorder.append(matrix[row_end][i])
            row_end -= 1
        if col_beg <= col_end:
            for i in range(row_end, row_beg -1, -1):
                spiralorder.append(matrix[i][col_beg])
            col_beg += 1

    return spiralorder

print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))