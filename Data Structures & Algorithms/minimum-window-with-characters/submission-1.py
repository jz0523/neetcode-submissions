class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        tCount = {}
        sCount = {}
        minlen = len(s) + 1
        res = (0, 0)

        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)

        l = 0
        have, need = 0, len(tCount)

        for r in range(len(s)):
            c = s[r]
            sCount[c] = 1 + sCount.get(c, 0)

            if c in tCount and sCount[c] == tCount[c]:
                have += 1
            
            while have == need:
                if r - l + 1 < minlen:
                    minlen = r - l + 1
                    res = (l, r)
                
                sCount[s[l]] -= 1
                if s[l] in tCount and sCount[s[l]] < tCount[s[l]]:
                    have -= 1
                
                l += 1
        
        if minlen > len(s):
            return ""
        else:
            return s[res[0]:res[1] + 1]
            
            


        