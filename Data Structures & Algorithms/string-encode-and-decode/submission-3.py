class Solution:

    def encode(self, strs: List[str]) -> str:
        out_str = []
        for i, word in enumerate(strs):
            out_str.append(word)
            out_str.append("、")
        return "".join(out_str)

    def decode(self, s: str) -> List[str]:
        out_str = []
        i = 0
        n = len(s)
        curr_str = []
        while i < n:
            if s[i] == "、":
                out_str.append("".join(curr_str))
                curr_str = []
                i += 1
                continue
            curr_str.append(s[i])
            i += 1
        return out_str