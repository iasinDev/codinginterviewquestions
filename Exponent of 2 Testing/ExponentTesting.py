import math

def solution(A):
    for value in A:
        if value < 0:
            result = str(value) + ': ' + str(0)
        elif value == 0:
            result = str(value) + ': ' + str(1)
        else:
            calc = math.log(value, 2) % 1
            if calc == 0:
                result = str(value) + ': ' + str(1)
            else:
                result = str(value) + ': ' + str(0)
        print(result)


solution([0, 1, 2, 4, 8, 14, 16, 64, 75, 0.5, 0.125, 0.1, -1, -2])
