def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    if len(states) == 0:
        return []
    current_states = states[:]
    for d in range(days):
        next_states = [None] * len(current_states)
        for i in range(len(current_states)):
            if i == 0 and len(current_states) > 2:
                next_states[i] = current_states[i+1] ^ 0
            elif i == len(current_states)-1:
                next_states[i] = current_states[i-1] ^ 0
            else:
                next_states[i] = current_states[i-1] ^ current_states[i+1]
        current_states = next_states[:]
    return current_states


print(cellCompete([1,0,0,0,0,1,0,0],0))
print(cellCompete([1,0,0,0,0,1,0,0],1))
print(cellCompete([1,1,1,0,1,1,1,1],2))