# def isValid(s):
#     stack = []
#     mapping = {")": "(", "}": "{", "]": "["}
#
#     for char in s:
#         # if char not in mapping dictionary keys, so it is opening parentheses
#         if char not in mapping:
#             stack.append(char)
#         else:
#             # fetch last element from stack
#             top_element = stack.pop() if stack else '#'
#             # compare last element from stack to the closing parentheses
#             # if not match return False
#             if mapping[char] != top_element:
#                 return False
#
#     return not stack
#
#
# print(isValid("{[]{()}}"))


# cheat solution
def balance_check(s):
    brackets = ['()', '{}', '[]']

    while any(x in s for x in brackets):
        for br in brackets:
            s = s.replace(br, '')

    return not s


out = balance_check("{[]{()}}")
print(out)
