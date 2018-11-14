INCOMPLETE = "incomplete"

def solution(N):
    return find_command_sequence(0, 1, N, "")


def find_command_sequence(L, R, N, command_sequence):
    if L == N or R == N:
        return command_sequence
    if abs(L) > abs(N) or abs(R) > abs(N):
        return INCOMPLETE

    resultL = find_command_sequence(2 * L - R, R, N, command_sequence + 'L')
    resultR = find_command_sequence(L, 2 * R - L, N, command_sequence + 'R')

    if resultL == INCOMPLETE and resultR == INCOMPLETE:
        return INCOMPLETE
    elif resultL == INCOMPLETE:
        return resultR
    elif resultR == INCOMPLETE:
        return resultL
    else:
        raise Exception("This should not happen")


for i in range(-100,100):
    print(i, solution(i))
