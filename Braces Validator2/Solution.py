# Complete the braces function below.
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

print(braces(["()[]{}", ")","()[]{","[{[]}]"]))
