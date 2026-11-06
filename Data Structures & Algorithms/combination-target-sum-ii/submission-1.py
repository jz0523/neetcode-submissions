class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, cur = [], []
        currsum = 0
        i = 0
        candidates.sort()

        def dfs(i, cur, currsum):
            if currsum == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or currsum > target:
                return
            
            #include the current element
            currelm = candidates[i]
            cur.append(currelm)
            dfs(i + 1, cur, currsum + currelm)
            cur.pop()
            while i < len(candidates) and candidates[i] == currelm:
                i += 1
            dfs(i, cur, currsum)
        
        dfs(0, cur, currsum)

        return res