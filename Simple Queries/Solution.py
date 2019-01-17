import bisect

def counts(nums, maxes):
    nums.sort()
    result = []
    for max in maxes:
        index = bisect.bisect_right(nums, max)
        result.append(index)
    return result


print(counts([1,4,2,4],[3,5]))
print(counts([2,10,5,4,8],[3,1,7,8]))