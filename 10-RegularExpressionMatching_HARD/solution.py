import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # Initialize DP table with False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty string matches empty pattern
        dp[0][0] = True

        # Handle patterns like a*, a*b*, etc. at the start
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # Fill the table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # Zero occurrence or match if preceding matches
                    dp[i][j] = dp[i][j - 2] or \
                            (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
                else:
                    # Match single character
                    dp[i][j] = dp[i - 1][j - 1] and \
                            (s[i - 1] == p[j - 1] or p[j - 1] == '.')

        return dp[m][n]
        