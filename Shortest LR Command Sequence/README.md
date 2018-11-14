# Shortest LR command sequence

Company| TopTal
---|---
Date|10/12/2018
Platform|Codility

You are given two integers L and R. Their values are initially set to L = 0 and R = 1.

You can change their values by performing the following commands:

* the command 'L' changes the value of L to 2 * L - R;
* the command 'R' changes the value of R to 2 * R - L;

You are given an integer N. The goal is to find the shortest sequence of commands after which L = N or R = N.

For example, consider N = -11: the shortest sequence of commands required to set either L or R to -11 is ['L','L','R','L']. After each command, the values of L and R are as follows:
* initial values: L = 0, R = 1;
* command 'L': L=-1, R=1;
* command 'L': L=-3, R=1;
* command 'R': L=-3, R=5;
* command 'L': L=-11, R=5;

After the fourth command we get L = N.

Write a function:

```python
def solution(N)
```
that given an integer N, returns a string describing the shortest sequence of commands required in order to set L = N or R = N. The string should comprise th names of the commands (i.e. characters 'L' and 'R') in the order of their execution. If there is more than one correct answer, the function may return any of them. 

The function should return the string "impossible" if the conditions L = N und R = N cannot arise.

For example, given N = -11, the function may return "LLRL", as explained above.

Write an __efficient__ algorithm for the following assumptions:
* N is an integer within the range [-2,147,483,648..2,147,483,647].