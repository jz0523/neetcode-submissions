class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #at any given slot in the 2n total slots, the number of ) cannot exceed the number of ( preceeding it.

        res, cur = [], []
        leftcnt, rightcnt = 0, 0
        def dfs():

            nonlocal leftcnt, rightcnt

            if len(cur) == 2 * n:
                if cur[-1] == ")" :
                    res.append("".join(cur.copy()))
                return
            
            #put a ( at this slot
            if leftcnt < n:
                cur.append("(")
                leftcnt += 1
                dfs()

                cur.pop()
                leftcnt -= 1

            #if we can put a ) at this slot, then we do
            if leftcnt > rightcnt:
                cur.append(")")
                rightcnt += 1
                dfs()
                cur.pop()
                rightcnt -= 1
        
        dfs()
        return res


            