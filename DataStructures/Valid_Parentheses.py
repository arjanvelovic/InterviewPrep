class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0
        while len(s) > 0:
            if s[0] in ['(', '{', '[']:
                stack.append(s[0])
            elif s[0] == ')' and (stack or [None])[-1] != '(' :
                return False
            elif s[0] == ')' and stack[-1] == '(':
                stack.pop()
            elif s[0] == ']' and (stack or [None])[-1] != '[' :
                return False
            elif s[0] == ']' and stack[-1] == '[':
                stack.pop()
            elif s[0] == '}' and (stack or [None])[-1] != '{' :
                return False
            elif s[0] == '}' and stack[-1] == '{':
                stack.pop()
            s = s[1:]
        if len(stack) > 0:
            return False
        return True