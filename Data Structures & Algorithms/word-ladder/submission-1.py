from collections import defaultdict
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        words = wordList.copy()
        words.append(beginWord)
        n = len(wordList)
        graph = defaultdict(list)
        for i, word1 in enumerate(words):
            for j in range(i + 1, n+1):
                word2 = words[j]
                diffcount = 0
                for x, y in zip(word1, word2):
                    if x != y:
                        diffcount += 1
                    if diffcount > 1:
                        break
                if diffcount == 1:
                    graph[word1].append(word2)
                    graph[word2].append(word1)

        #do bfs
        level = 1
        q = deque([beginWord])
        visited = set([beginWord])
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return level
                
                for neighbor in graph[word]:
                    if neighbor in visited:
                        continue
                    visited.add(neighbor)
                    q.append(neighbor)

            level += 1
        
        return 0