# Maximum Difference in Array

Company| iPsY
---|---
Date|11/8/2018
Platform|HackerRank

You are given an array of integers and must compute the maximum difference between any item and any lower indexed smaller item for all the possible pairs, i.e., for a given array _a_ find the maximum value of _a[j] - a[i]_ for all _i,j_ where _0<=i<j<n_ and _a[i] < a[j]_. If no item has a smaller item with a lower index then return -1.

For example given an array [1,2,6,4], you would first compare 2 to the elements to its left. 1 is smaller, so calulcate the difference 2 -1 = 1. 6 is bigger than 2 and 1, so calculate the differences 4 and 5. 4 is only bigger than 2 and 1, and the differences are 2 and 3. The largest difference was 6 -1 = 5.

#### Function Descritpion

Complete the function maxDifference in the editor below. The function must return an integer representing the maximum difference in _a_.

maxDifference has the following parameter(s):
 _a[a[0],a[1],...a[n]]:_ an array of integers

 #### Constraints
 * _1<= n <=2 * 10^5_
 * _-10^6 <= a[i] <= 10^6 i is of [0, n-1]_