# Power of 10?

Company|Goldman Sachs
---|---
Date|01/25/2019
Platform|CoderPad.io

Check if a number is a power of 10.

For example 10^1=10, 10^2=100, 10^3=1000 are number of power of 10.

```python
def isPowerOf10(x):
    while x != 0 and x % 10 == 0:
        x //= 10
    return x == 1
```