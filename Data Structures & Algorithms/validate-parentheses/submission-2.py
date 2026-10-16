class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for p in s:
            if p not in pairs:
                stack.append(p)
                continue
            else:
                if not stack or pairs[p] != stack[-1]:
                    return False
                stack.pop()
        
        return not stack
                