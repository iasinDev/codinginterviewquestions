# My solution does not give 100% correct results

def solution(A):
    # write your code in Python 3.6
    max_length = 0
    visited = [False] * len(A)
    for i in range(0, len(A)):
        max_length = max(max_length, test(A, i, visited, 0))
    return max_length

def test(A,i,visited,length):
    if visited[i]:
        return length
    else:
        visited[i] = True
        if A[i]>=len(A):
            return length
        else:
            return test(A, A[i], visited, length+1)

print(solution([5,4,0,3,1,6,2]) == 4)
print(solution([]) == 0)
print(solution([0]) == 1)
print(solution([1]) == 0)