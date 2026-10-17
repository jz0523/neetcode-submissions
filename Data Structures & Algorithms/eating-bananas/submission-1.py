class Solution:
    def calTime(self, k, piles) -> int:
        time = 0
        for x in piles:
            time += (x + k - 1) // k
        return time

    def binSearch(self, piles, l, r, h):
        if l > r:
            return l
        med = (l + r) // 2
        time = self.calTime(med, piles)

        if time > h:
            return self.binSearch(piles, med + 1, r, h)
        else:
            return self.binSearch(piles, l, med - 1, h)

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxk = max(piles)

        k = self.binSearch(piles, 1, maxk, h)
        return k
