class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, partition = [], []

        def checkPalin(string):
            l, r = 0, len(string) - 1
            while l < r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i):
            if i >= len(s):
                res.append(partition.copy())
                return
            
            for j in range(i, len(s)):
                string = s[i:j+1]
                if checkPalin(string):
                    partition.append(string)
                    dfs(j + 1)
                    partition.pop()
        
        dfs(0)
        return res


            
