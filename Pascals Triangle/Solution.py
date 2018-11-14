# Return values of pascals triangle in an array
#     1
#    1 1
#   1 2 1
#  1 3 3 1

# input: depth = d
# output: [ 1 1 1 1 2 1 1 3 3 1 ]
def solution(d):
    if d < 1:
        return []
    result = []
    last_array = []
    for i in range(1, d + 1):
        array = [None] * i
        for j in range(i):
            if j == 0 or j == i - 1:
                array[j] = 1
            else:
                array[j] = last_array[j - 1] + last_array[j]
        last_array = array
        result.extend(array)
    return result


print(solution(-1))
print(solution(0))
print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
