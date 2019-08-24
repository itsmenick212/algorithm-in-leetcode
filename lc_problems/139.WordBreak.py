class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(dp)):
            for w in wordDict:
                if i >= len(w) and dp[i-len(w)] and s[i-len(w):i] == w:
                    dp[i] = True
        return dp[-1]

