class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        n = len(s)
        left, right = 0, 0
        currentCost = 0
        maxLen = 0

        while right < n:
            currentCost += abs(ord(s[right]) - ord(t[right]))
            while currentCost > maxCost:
                currentCost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            maxLen = max(maxLen, right - left + 1)
            right += 1

        return maxLen
    
solution = Solution()
# print(solution.equalSubstring('abcd', 'acde', 0))
print(solution.equalSubstring('krrgw', 'zjxss', 19))