class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def cal(num1, num2, op:str):
            if op == "+":
                return num1 + num2
            elif op == "-":
                return num1 - num2
            elif op == "*":
                return num1 * num2
            elif op == "/":
                return int(num1 / num2)
            else:
                return None
        
        ops = {"+", "-", "*", "/"}
        stack = []
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
                continue
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                num = cal(num1, num2, t)
                stack.append(num)
        
        return stack[0]