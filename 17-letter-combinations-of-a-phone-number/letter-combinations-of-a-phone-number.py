class Solution:
    def letterCombinations(self, digits: str):

        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtrack(index, path):

            # Combination complete
            if index == len(digits):
                result.append(path)
                return

            # Current digit letters
            letters = phone[digits[index]]

            for ch in letters:
                backtrack(index + 1, path + ch)

        backtrack(0, "")

        return result