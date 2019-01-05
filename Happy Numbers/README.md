# Happy Numbers


Company| J.P. Morgan Chase
---|---
Date|12/7/2018
Platform|HireVue

A happy number is defined by the following process. Start with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1(where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers.

## Input

Your program should read lines of thext from standard input. Each line contains a single positive integer, N.

## Output
If the number is a happy number, print 1 to standard output. Otherwise, print 0.

For the curious, here's why 7 is a happy number: 7 -> 49 -> 97 -> 130 -> 10 -> 1. Here's why 22 is NOT a happy number: 22 -> 8 -> 64 -> 52 -> 29 -> 85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89.

## Test 1

### Input
1

### Output
1

## Test 2

### Input 
22

### Output
0

## Follow-up question with a video recorded answer
If happy numbers are generally prime(19, 79, 239) should it always end in a 9? Can you think of a happy number that doesn't end in 9?

### My answer
(not sure if it's correct)
7 is also a prime number and it doesn't end on 9. On the wikipedia article about [happy numbers](https://en.wikipedia.org/wiki/Happy_number) I found that all prime numbers are happy numbers. And not every prime number ends on a 9.