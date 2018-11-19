# Sprial Matrix
def iterate_over_matrix(matrix):
    height = len(matrix)
    if height < 1:
        return []
    width = len(matrix[0])
    result = []
    h = 0
    w = 0
    while w < int(width/2)+1 and h < int(height/2)+1:
        if height != 2 or h != 1:
            for k in range(w, width-w):
                result.append(matrix[h][k])
        h += 1
        if width != 2 or w != 1:
            for k in range(h, height-h+1):
                result.append(matrix[k][width-w-1])
        w += 1
        if h < int(height/2)+1:
            for k in range(width-w-1, w-2, -1):
                result.append(matrix[height-h][k])
        if w < int(width/2)+1:
            for k in range(height-h-1, h-1, -1):
                result.append(matrix[k][w-1])
    return result


print(iterate_over_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5])
print(iterate_over_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10])
print(iterate_over_matrix([]) == [])
print(iterate_over_matrix([[]]) == [])
print(iterate_over_matrix([[3]]) == [3])
print(iterate_over_matrix([[3], [2]]) == [3, 2])
print(iterate_over_matrix([[4], [3], [2], [1]]) == [4, 3, 2, 1])
print(iterate_over_matrix([[1,2], [8,3], [7,4], [6,5]]) == [1,2,3,4,5,6,7,8])
print(iterate_over_matrix([[1, 2, 3, 4]]) == [1, 2, 3, 4])
print(iterate_over_matrix([[2, 5, 8], [4, 0, -1]]) == [2, 5, 8, -1, 0, 4])
print(iterate_over_matrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]) == [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13])
