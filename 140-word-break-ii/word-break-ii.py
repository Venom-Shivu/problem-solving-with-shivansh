class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        memo = {}

        def backtrack(start):
            if start == len(s):
                return [""]

            if start in memo:
                return memo[start]

            sentences = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in words:
                    rest_sentences = backtrack(end)

                    for rest in rest_sentences:
                        if rest:
                            sentences.append(word + " " + rest)
                        else:
                            sentences.append(word)

            memo[start] = sentences
            return sentences

        return backtrack(0)