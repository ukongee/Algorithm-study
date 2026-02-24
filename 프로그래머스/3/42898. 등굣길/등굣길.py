
def solution(m: int, n: int, puddles) -> int:
    MOD = 1000000007
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # puddles 마킹 (x,y)
    for x, y in puddles:
        dp[y][x] = -1

    # 시작/도착이 웅덩이면 0
    if dp[1][1] == -1 or dp[n][m] == -1:
        return 0

    dp[1][1] = 1

    for i in range(1, n + 1):      # y
        for j in range(1, m + 1):  # x
            if dp[i][j] == -1:
                dp[i][j] = 0
                continue
            if i == 1 and j == 1:
                continue

            dp[i][j] = (dp[i][j] + dp[i - 1][j]) % MOD
            dp[i][j] = (dp[i][j] + dp[i][j - 1]) % MOD

    return dp[n][m]