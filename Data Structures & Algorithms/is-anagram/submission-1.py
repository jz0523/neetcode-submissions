from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)
        for char in s:
            count[char] += 1
        
        for char in t:
            count[char] -= 1
            if count[char] < 0:
                return False
        
        for char in s:
            if count[char] != 0:
                return False
        
        return True