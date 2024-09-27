class Solution(object):
    def isValid(self, s):
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map.keys():
                if stack and stack[-1] == bracket_map[char]:
                    stack.pop()
                else:
                    return False

        return not stack
