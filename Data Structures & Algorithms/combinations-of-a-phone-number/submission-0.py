class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res, cur = [], []
        lookup = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i):
            if i >= len(digits):
                res.append("".join(cur.copy()))
                return
            
            dig = digits[i]
            #loop through all possible elment at this index
            for char in lookup[dig]:
                cur.append(char)
                dfs(i + 1)
                cur.pop()
            
        dfs(0)
        if not digits:
            return []

        return res
