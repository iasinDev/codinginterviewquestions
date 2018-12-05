# Check if Number is Exponent of 2

Company| Monsanto
---|---
Date|10/16/2018
Platform| Filtered.ai

Check if an given number is an exponent of 2. For example 8 is 2^3 so. 0.5 is 2^-1 and is also an exponent of 2. 64 is an exponent of 2 because 2^6.

This is the solution I came up with. I am not sure about negative values. This solution scored 90% better than average and seems to be ok.

```python
import math

def solution(A):
    for value in A:
        if value < 0:
            result = str(value) + ': ' + str(0)
        elif value == 0:
            result = str(value) + ': ' + str(1)
        else:
            calc = math.log(value, 2) % 1
            if calc == 0:
                result = str(value) + ': ' + str(1)
            else:
                result = str(value) + ': ' + str(0)
        print(result)
```