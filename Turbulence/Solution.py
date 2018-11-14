# This is a false solution. I don't understand the problem in all details. Especially I don't understand why [4,8,12,16] is a turbulence.

def solution(A):
    if len(A)==0:
        return 0
    if len(A)==1:
        return 1 # by definition?
    if len(A)==2:
        return 0   # not sure
    turbulence_max = 0
    turbulence_current = 0
    for i in range(2,len(A)):
        if A[i-2] < A[i-1] > A[i] or A[i-2] > A[i-1] < A[i]:
            if turbulence_current == 0:
                turbulence_current+=3
            else:
                turbulence_current+=1
        else:
            if turbulence_current > turbulence_max:
                turbulence_max = turbulence_current
            turbulence_current = 0
    if turbulence_current > turbulence_max:
        turbulence_max = turbulence_current
    return turbulence_max



print(solution([9,4,2,10,7,8,8,1,9])) # ok
print(solution([100])) # ok
print(solution([50,150,50,150,50,150])) # ok
print(solution([4,8,12,16])) # incorrect result; according to the examples
                             # the result should be 2 what I don't understand.
                             # 0 seems to be the correct result to me
