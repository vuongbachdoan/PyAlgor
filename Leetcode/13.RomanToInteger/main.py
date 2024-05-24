class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,  # Subtractive cases
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        result = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in roman_map:  # Check for subtractive cases
                result += roman_map[s[i:i+2]]
                i += 2
            else:
                result += roman_map[s[i]]
                i += 1

        return result

# Example usage
solution = Solution()
print(solution.romanToInt("MCMXCIV"))  # Output: 1994
