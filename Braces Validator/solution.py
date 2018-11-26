# Validate strings like
# '()[]{}' => true
# '({[]})' => true
# '({])' => false
# ')' => false

def bracket_validator(str):
    stack = []
    for i, c in enumerate(str):
        if is_opening_bracket(c):
            stack.append(c)
        else:
            if len(stack) > 0:
                temp = is_same_type_of_bracket(c, stack.pop())
                if temp is not True:
                    return False
            else:
                return False
    if len(stack) > 0:
        return False
    return True

def is_same_type_of_bracket(character, stack):
    return (character == ')' and stack == '(') or (character == ']' and stack == '[') or (character == '}' and stack == '{')


def is_opening_bracket(char):
    return char in ['(', '[', '{']


def is_closing_bracket(char):
    return char in [')', ']', '}']

# def bracket_validator_recursive(str):
#     i = 0
#     while i < len(str):
#         if is_opening_bracket(str[i]):
#             result = bracket_validator_recursive_(str[i + 1:len(str)], str[i])
#             if result < 0:
#                 return False
#             else:
#                 i += result
#
#
# def bracket_validator_recursive_(str, stack, ):
#     if len(str) <= 0:
#         return -1
#     result = 0
#     if is_opening_bracket(str[0]):
#         result = bracket_validator_recursive_(str[1:len(str)], str[0])
#         if result > 0:
#             result +=1
#     if is_closing_bracket(str[0]):
#         if
#     return result



# print(bracket_validator('()[]{}'))
# print(bracket_validator('({[]})'))
print(bracket_validator('({[]})()'))
print(bracket_validator('({[]})(]'))
# print(bracket_validator('({])'))
# print(bracket_validator('()'))
# print(bracket_validator(')'))
