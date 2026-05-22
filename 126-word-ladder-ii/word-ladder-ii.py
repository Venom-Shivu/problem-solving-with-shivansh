from collections import defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str,
                    wordList: List[str]) -> List[List[str]]:

        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

        parents = defaultdict(list)

        level = {beginWord}
        found = False

        while level and not found:
            next_level = set()

            wordSet -= level

            for word in level:
                chars = list(word)

                for i in range(len(word)):
                    original = chars[i]

                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        chars[i] = c
                        new_word = ''.join(chars)

                        if new_word in wordSet:
                            if new_word == endWord:
                                found = True

                            next_level.add(new_word)
                            parents[new_word].append(word)

                    chars[i] = original

            level = next_level

        if not found:
            return []

        result = []
        path = [endWord]

        def dfs(word):
            if word == beginWord:
                result.append(path[::-1])
                return

            for parent in parents[word]:
                path.append(parent)
                dfs(parent)
                path.pop()

        dfs(endWord)

        return result