class Solution:
    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:

        words = set(wordList)

        if endWord not in words:
            return 0

        begin = {beginWord}
        end = {endWord}

        length = 1
        letters = 'abcdefghijklmnopqrstuvwxyz'

        while begin:
            # Expand smaller side
            if len(begin) > len(end):
                begin, end = end, begin

            next_level = set()

            for word in begin:
                chars = list(word)

                for i in range(len(word)):
                    original = chars[i]

                    for c in letters:
                        chars[i] = c
                        new_word = ''.join(chars)

                        if new_word in end:
                            return length + 1

                        if new_word in words:
                            next_level.add(new_word)
                            words.remove(new_word)

                    chars[i] = original

            begin = next_level
            length += 1

        return 0