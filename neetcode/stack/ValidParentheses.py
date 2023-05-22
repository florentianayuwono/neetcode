class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        while len(s) > 0:
            curr_char = s[-1]
            if curr_char == '}' or curr_char == ']' or curr_char == ')':
                stack.append(curr_char)
            else:
                if len(stack) == 0:
                    return False
                stack_char = stack.pop()
                if curr_char == '(' and stack_char != ')':
                    return False
                if curr_char == '{' and stack_char != '}':
                    return False
                if curr_char == '[' and stack_char != ']':
                    return False
            s = s[:-1]
        if len(stack) > 0:
            return False
        return True
