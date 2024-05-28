class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        count = 0
        for num in nums1:
            for num2 in nums2:
                if num2 != 0 and num % (num2 * k) == 0:
                    count += 1
                elif num2 == 0 and num == 0:
                    count += 1
        return count
