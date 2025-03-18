class Solution:
    def romanToInt(self, s: str) -> int:
        char_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        reversed_str = s[::-1]
        ans = char_to_int[reversed_str[0]]

        for i in range(len(reversed_str)-1):
            if char_to_int[reversed_str[i+1]] >= char_to_int[reversed_str[i]]:
                ans = ans + char_to_int[reversed_str[i+1]]
            else:
                ans = ans - char_to_int[reversed_str[i+1]]

        return ans