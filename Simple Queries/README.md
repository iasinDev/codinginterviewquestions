# Twin Strings

Company| Flextrade
---|---
Date|01/17/2019
Platform|HackerRank

Given two arrays of positive integers, for each element in the second array, find the total number of elements in the first array which are _less than_ or _equal to_ that element. Store the values determined in an array.

For example, if the first array is _[1,2,3]_ and the second array is _[2,4]_, then there are 2 elements in the first array _less than_ or _equal to_ 2. There are _3_ elements in the first array which are _less than_ or _equal to_ 4. We can store these answers in an array, _answer = [2,3]_.

### Function Description
Complete the function _counts_ in the editor below. The function must return an array of _m_ positive integers, one for each _maxes[i]_ representing the total number of elements _nums[i]_ satisfying _nums[j] <= maxes[i]_ where _0 <= j < n_ and _0 <= i < m_, in the given order.

counts has the following parameter(s):
* _nums[nums[0],...nums[n-1]]:_ first array of positive integers
* _maxes[maxes[0],...maxes[n-1]]:_ second array of positive integers

#### Constraints
* 2 <= n,m <= 10^5
* 1 <= nums[j] <= 10^9, where 0 <= j < n.
* 1 <= maxes[i] <= 10^9, where 0 <= i < m.
* Runtime should be O(N) for full score. Less optimized solutions will receive partial score.

### Sample Case 0
#### Sample Input 0
```
4
1
4
2
4
2
3
5
```
#### Sample Output 0
```
2
4
```

#### Explanation 0
We are given n = 4, nums = [1,4,2,4], m = 2, and _maxes = [3,5]_.
1. For _maxes[0] = 3_, we have **2** elements in _nums(nums[0] = 1_ and _nums[2] = 2_) that are <= _maxes[0]_.
2. For _maxes[1] = 5_, we have **4** elements in _nums(nums[0] = 1_, _nums[1] = 4, _nums[2] = 2_ and _nums[3] = 4_) that are <= _maxes[1]_.

Thus, the function returns the array _[2,4]_ as the answer.

### Sample Case 1
#### Sample Input 1
```
5
2
10
5
4
8
4
3
1
7
8
```
#### Sample Output 1
```
1
0
3
4
```

#### Explanation 1
We are given, n = 5, nums = [2,10,5,4,8], m = 4, and _maxes = [3,1,7,8]_.
1. For _maxes[0] = 3_, we have **1** elements in _nums(nums[0] = 2_) that is <= _maxes[0]_.
2. For _maxes[1] = 1_, we have **0** elements in _nums_ that are <= _maxes[1]_
3. For _maxes[2] = 7_, we have **3** elements in _nums(nums[0] = 2_, _nums[2] = 5_ and _nums[3] = 4_) that are <= _maxes[2]_.
3. For _maxes[3] = 8_, we have **4** elements in _nums(nums[0] = 2_, _nums[2] = 5_, _nums[3] = 4_ and nums[4] = 8) that are <= _maxes[3]_.

Thus, the function returns the array _[1,0,3,4]_ as the answer.


### Solution
**O((m+n) log n) solution. This is not the optimal solution but I didn't notice any runtime timeouts during the tests.**
```python
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
```