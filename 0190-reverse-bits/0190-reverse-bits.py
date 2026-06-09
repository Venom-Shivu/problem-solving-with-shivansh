class Solution:
    table = [0] * 256

    for i in range(256):
        x = i
        rev = 0
        for _ in range(8):
            rev = (rev << 1) | (x & 1)
            x >>= 1
        table[i] = rev

    def reverseBits(self, n: int) -> int:
        return (
            (self.table[n & 255] << 24) |
            (self.table[(n >> 8) & 255] << 16) |
            (self.table[(n >> 16) & 255] << 8) |
            (self.table[(n >> 24) & 255])
        )