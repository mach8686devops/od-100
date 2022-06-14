# 路灯问题

while 1:
    try:
        n = int(input())
        nums = list(map(int, input().split(",")))

        dp = [0] * (n-1)

        def funcl(i, w):
            if w > 0 and i >= 0:
                dp[i] = min(100, dp[i] + w)
                funcl(i - 1, w - 100)

        def funcr(i, w):
            if w > 0 and i < n-1:
                dp[i] = min(100, dp[i] + w)
                funcr(i + 1, w - 100)

        for i in range(n):
            funcl(i-1, nums[i])
            funcr(i, nums[i])

        print((n-1)*100 - sum(dp))
    except Exception as e:
        break
