# My solution does not give 100% correct results

def solution(A):
    # write your code in Python 3.6
    max_length = 0
    for i in range(0, len(A)):
        length = test(A, i, {}, 0)
        if length > max_length:
            max_length = length
    return max_length

def test(A,i,visited,length):
    if i in visited:
        return length
    else:
        visited[i] = 'true'
        if A[i]>=len(A):
            return length
        else:
            return test(A, A[i], visited, length+1)

print(solution([5,4,0,3,1,6,2]))
print(solution([]))
print(solution([0]))
print(solution([1]))