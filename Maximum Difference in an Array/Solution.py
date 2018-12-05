# My solution failed to test cases during the coding challenge.
# Now this is the improved solution
# I guess that I forgot to handle the equal case well
# like: maxDifference([6,6])==-1 and not 0
def maxDifference(a):
    maximum_value = -1
    minimum_value = a[0]
    for i in range(1,len(a)):
        if a[i]-minimum_value > 0:
            maximum_value = max(maximum_value, a[i]-minimum_value)
        minimum_value = min(minimum_value, a[i])
    return maximum_value

print(maxDifference([1,2,6,4])==5)
print(maxDifference([1,6])==5)
print(maxDifference([6,1])==-1)
print(maxDifference([6,6])==-1)
print(maxDifference([-10,-1])==9)
print(maxDifference([2,6,4,7,1,2])==5)
print(maxDifference([4,3,2,1])==-1)
print(maxDifference([1])==-1)
print(maxDifference([5])==-1)
print(maxDifference([-1,-2,-5,-10,2])==12)
print(maxDifference([-1,-2,-5,-10])==-1)