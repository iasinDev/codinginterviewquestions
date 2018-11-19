# Iterate over Matrix

def iterate_over_matrix(matrix):
    l = len(matrix)
    result = []
    for i in range(int(l/2)+1):
        for j in range(i,l-i):
            result.append(matrix[i][j])
        for j in range(i+1,l-i):
            result.append(matrix[j][l-i-1])
        for j in range(l-i-2,i-1, -1):
            result.append(matrix[l-i-1][j])
        for j in range(l-i-2,i, -1):
            result.append(matrix[j][i])
    return result

# print(iterate_over_matrix([[1,2,3],[4,5,6],[7,8,9]]))
# print(iterate_over_matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
print(iterate_over_matrix([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]))

