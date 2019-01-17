# Twin Strings

Company| Flextrade
---|---
Date|01/17/2019
Platform|HackerRank

Two string are said to be _twins_ only if they can be made equivalent by performing some number of operations on one or both strings. There are two possible operations:

* SwapEven: Swap a character at an even-numbered index with a character at another even-numbered index.
* SwapOdd: Swap a character at an odd-numbered index with a character at another odd-numbered index.

For example, given the array [5,6,7,8], you coud swap elements at values 5 and 7 to get [7,6,5,8]. You could also swap 6 and 8.

You will be given multiple pairs of strings to test and must return an array of strings either "Yes" or "No" based on wheather they are twins. There should be one string added to the array per test in the order the pairs are given.

### Function Description
Complete the function _twins_ in the editor below. The function must return an array of strings where each index _i_ (0 <= i < n) contains the string Yes if _a[i]_ and _b[i]_ are twins or the string No if they are not.

twins has the following parameter(s):
* _a[a[0],...,a[n-1]]:_ first array of strings
* _b[b[0],...,b[n-1]]:_ second array of strings

#### Constraints
* 1 <= n <= 10^3
* 1 <= |_a[i]_|, |_b[i]_| <= 100
* _a[i]_ and _b[i]_ are not guaranteed to have the same length (|a[i]| may not equal |b[i]|).
* Strings _a[i]_ and _b[i]_ contain lowercase letters only, in the range ascii[a-z].

### Sample Case 0
#### Sample Input 0
```
3
cdab
dcba
abcd
3
abcd
abcd
abcdcd
```
#### Sample Output 0
```
Yes
No
No
```

#### Explanation 0
Given a = ["cdab","dcba","abcd"] and b = ["abcd","abcd","abcdcd"], we process each element as follows:
1. _a[0]_ = "cdab" and _b[0]_ = "abcd": We store Yes in index 0 of the return array because a[0] = "**c**d**a**b" -> "a**d**c**b**" -> "abcd" = b[0]
2. _a[1]_ = "cdab" and _b[1]_ = "abcd": We store No in index 1 of the return array because no amount of operations will move a character from an odd index to an even index, so the two string will never be equal.
3. _a[2]_ = "abcd" and _b[2]_ = "abcdcd": We store No in index 2 of the return array. There is not operation to move a character into a new position in _a[2]_, so the two strings will never be equal.

We then return the array ["Yes", "No", "No"] as our answer.

### Solution
```python
def twins(a, b):
    result = []
    for i in range(len(a)):
        aEven, aOdd = [], []
        for j in range(len(a[i])):
            if j % 2 == 0:
                aEven.append(a[i][j])
            else:
                aOdd.append(a[i][j])
        aEven.sort()
        aOdd.sort()
        bEven,bOdd = [],[]
        for j in range(len(b[i])):
            if j%2==0:
                bEven.append(b[i][j])
            else:
                bOdd.append(b[i][j])
        bEven.sort()
        bOdd.sort()
        result.append("Yes" if aEven == bEven and aOdd == bOdd else "No")
    return result

print(twins(["cdab", "dcba", "abcd"],["abcd", "abcd", "abcdcd"]))

```