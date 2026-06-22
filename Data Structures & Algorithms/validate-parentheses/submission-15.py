class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s)%2!=0:
            return False
        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if not stack:
                    return False
                if c == "}" and stack[-1] == "{":
                    stack.pop()
                    continue
                if c == "]" and stack[-1] == "[":
                    stack.pop()
                    continue
                if c == ")" and stack[-1] == "(":
                    stack.pop()
                    continue
                return False
        return not stack

            
            