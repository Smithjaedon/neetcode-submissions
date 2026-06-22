class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if not stack:
                    return False
                if c == "}" and stack[-1] != "{":
                    return False
                if c == "]" and stack[-1] != "[":
                    return False
                if c == ")" and stack[-1] != "(":
                    return False
                stack.pop()
        return not stack

            
            