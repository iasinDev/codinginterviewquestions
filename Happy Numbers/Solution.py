import sys
from collections import defaultdict

def happyNumber(a):
    memory = defaultdict(int)
    value = int(a)
    while memory[value]<=1 and memory[1]==0:
        sum = 0
        for digit in str(value):
            sum+=int(digit)**2
        memory[sum]+=1
        value=sum
    return memory.get(1,0)>0

# for line in sys.stdin:
#     print(1 if happyNumber(line) else 0)

print(happyNumber("1") == True)
print(happyNumber("7") == True)
print(happyNumber("22") == False)
print(happyNumber("49") == True)