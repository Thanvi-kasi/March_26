class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        
        # DP table
        dp = [[0] * n for _ in range(m)]
        
        # Base case: princess cell
        dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])
        
        # Last column
        for i in range(m-2, -1, -1):
            dp[i][n-1] = max(1, dp[i+1][n-1] - dungeon[i][n-1])
        
        # Last row
        for j in range(n-2, -1, -1):
            dp[m-1][j] = max(1, dp[m-1][j+1] - dungeon[m-1][j])
        
        # Fill remaining cells
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                need = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
                dp[i][j] = max(1, need)
        
        return dp[0][0]
