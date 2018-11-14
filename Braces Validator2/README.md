# Braces

Company| Ascend.io
---|---
Date|11/12/2018
Platform|HackerRank

You are designing a compiler for a C++ program and need to check that braces in any given file are balanced.

Braces in a string are considered to be balanced if the following criteria are met:
* All braces must be closed. Braces come in pairs of the form (),{} and []. The left brace opens the pair, and the right one closes it.
* In any set of nested braces, the braces between any pair must be closed.

For example, `[{}]` is a vaild grouping of braces but `[}]{}` is not.

### Function Description
Comelete the function _braces_ in the editor below. The function must return an array of string where the string at each index i denotes whether or not the braces were balanced in a _valuesi_. The array should consist of strings "YES" or "NO" aligned with their indexes in _values_.

braces has the following parameters(s):
    _values[values0, ... valuesn-1]:_ an array of strings to anyalyze

### Constraints
* 1 <= n <= 15
* 1 <= length of valuesi <= 100
* it is guaranteed that each values i, consists of (, ), {,},[,] only.

### Sample Case 0
#### Sample Input For Custom Testing
```
2
{}[]()
{[}]}
```
#### Sample Output

```
YES
NO
```

#### Explanation
values 0: {}[]() meets the criteria for a balanced string, so index 0 in our return array should contain the string YES.
values 1: {[}]} contains unmatched braces between a matched pair in the substrings [},{[}, and [}], so index 1 in our return array should contain the string NO

### Solution

My Python solution matched a 100% of the testcases.

```
def braces(values):
    result = []
    for braces_string_to_check in values:
        result.append(check(braces_string_to_check))
    return result

def check(braces_string):
    stack = []
    for brace in braces_string:
        if brace in ['(','{','[']:
            stack.insert(0, brace)
        elif brace in [')','}',']']:
            if len(stack) > 0:
                last_opening_brace = stack.pop(0)
                if (brace == ')' and last_opening_brace != '(') or (brace == '}' and last_opening_brace != '{') or (brace == ']' and last_opening_brace != '['):
                    # brace doesn't fit to previous brace
                    return "NO"
            else:
                # stack empty / starting with a closing brace
                return "NO"
        else:
            # invalid character
            return "NO"
    if len(stack) > 0:
        # still braces left on stack / invalid amount of closing braces
        return "NO"
    return "YES"    
```