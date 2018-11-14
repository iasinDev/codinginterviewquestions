# Longest Turbulence

Company|TopTal
---|---
Date|10/12/2018
Platform| Codility

Your team is analysing a flight plane. Your task is to find the longest period of turbulence.

The height of the plane above the ground is measured once every second of th flight. The measurement on K-th second is recoreded as an integer A[K].

Security regulations decree that a period of time is considered to be turbulence if changes in measured heights alternate: for example, if the plane went up, then down, then up and so on.

Most precisely, period (P,Q) is considered to be an turbulence if:

* A[P] > A[P+1] < A[P+2] > ..., and so on, up to A[Q] or
* A[P] < A[P+1] > A[P+2] < ..., and so on, up to A[Q]

Note that, for definition, if P = Q then the period is also considered to be turbulence.

Write a function: 

def solution(A)

that, given an array A consisting of N integers representing height measurements during the flight, return the size of the longest period of turbulence in A.

Examples:

1. Given array A = [9,4,2,10,7,8,8,1,9] the function should return 5, because period (1,5) is considered to be turbulence (A[1] > A[2] < A[3] > A[4] < A[5]). Note that period (1,6) is not turbulence, because A[5] = A[6].

2. Given array A = [4,8,12,16] the function should return 2.

3. Given array A = [100] the function should return 1.

4. Given N = 100,000 and A = [50,150,50,150,...,50,150] ([50,150] repeating 50,000 times) the function should return 100,000.

Write an efficient algorithm for the following assumptions:
* N is an integer within the range [1...100,000];
* each element of array A is an integer within the range [1..1,000,000,000].

# Comment
I don't understand why the second array [4,8,12,16] is a turbulence which follows the definition of a turbulence
* A[P] > A[P+1] < A[P+2] > ..., and so on, up to A[Q] or
* A[P] < A[P+1] > A[P+2] < ..., and so on, up to A[Q] 

