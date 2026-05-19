class Solution:
    def fullJustify(self, words, maxWidth):

        result = []

        i = 0
        n = len(words)

        while i < n:

            line_length = len(words[i])
            j = i + 1

            # Find how many words fit
            while (
                j < n and
                line_length + 1 + len(words[j]) <= maxWidth
            ):
                line_length += 1 + len(words[j])
                j += 1

            line_words = words[i:j]
            num_words = j - i

            # Last line or single word
            if j == n or num_words == 1:

                line = " ".join(line_words)

                line += " " * (maxWidth - len(line))

            else:

                total_chars = sum(len(word) for word in line_words)

                total_spaces = maxWidth - total_chars

                gaps = num_words - 1

                even_spaces = total_spaces // gaps

                extra_spaces = total_spaces % gaps

                line = ""

                for k in range(gaps):

                    line += line_words[k]

                    spaces = even_spaces

                    if k < extra_spaces:
                        spaces += 1

                    line += " " * spaces

                line += line_words[-1]

            result.append(line)

            i = j

        return result