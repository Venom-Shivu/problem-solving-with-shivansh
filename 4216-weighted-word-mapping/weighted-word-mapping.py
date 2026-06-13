from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        w = [0] * 123

        for i in range(26):
            w[i + 97] = weights[i]

        res = []
        append = res.append

        for word in words:
            total = 0
            for ch in word:
                total += w[ord(ch)]

            append(chr(122 - (total % 26)))

        return ''.join(res)