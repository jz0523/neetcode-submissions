from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        allval = self.timemap[key]
        n = len(allval)
        l, r = 0, n - 1
        if timestamp < allval[0][1]:
            return ""

        while l <= r:
            leftval = allval[l][1]
            rightval = allval[r][1]
            mid = (l + r) // 2
            midval = allval[mid][1]

            if midval == timestamp:
                return allval[mid][0]
            elif midval > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        
        return allval[r][0]

        
