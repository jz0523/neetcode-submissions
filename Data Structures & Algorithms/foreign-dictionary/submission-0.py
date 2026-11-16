from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c: set() for w in words for c in w}
        n = len(words)
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i+1]
            minLen = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""
            for j in range(minLen):
                if word1[j] != word2[j]:
                    graph[word1[j]].add(word2[j])
                    break
        
        visited = {}
        res = []
        def dfs(char):
            if char in visited:
                return visited[char]
            
            visited[char] = True

            for nei in graph[char]:
                if dfs(nei):
                    return True
            
            visited[char] = False

            res.append(char)
        
        for c in graph:
            if dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)
