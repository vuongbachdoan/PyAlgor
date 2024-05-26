class Solution:
    def compressedString(self, word: str) -> str:
        res = []
        i = 0
        while i < len(word):
            count = 1
            while i + 1 < len(word) and word[i] == word[i+1] and count < 9:
                i += 1
                count += 1
            res.append(str(count) + word[i])
            i += 1
        return ''.join(res)
