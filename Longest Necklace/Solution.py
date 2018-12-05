# My solution does not give 100% correct results

def solution(A):
    # write your code in Python 3.6
    max_length = 0
    visited = [False] * len(A)
    for i in range(0, len(A)):
        j = i
        length = 0
        while j < len(A) and not visited[j]:
            visited[j] = True
            length+=1
            j = A[j]
        max_length = max(max_length, length)
    return max_length

print(solution([5,4,0,3,1,6,2]) == 4)
print(solution([]) == 0)
print(solution([0]) == 1)
print(solution([1]) == 1)