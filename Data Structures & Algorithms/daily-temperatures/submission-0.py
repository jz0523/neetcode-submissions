class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                elm = stack.pop()
                count = i - elm[1]
                res[elm[1]] = count
            stack.append((temp, i))
        return res