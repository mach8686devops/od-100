# 字符串漂亮度
counts = list(range(26, 1, -1))
while 1:
    try:
        dp = {}
        for c in input().lower():
            if c in dp:
                dp[c] += 1
            else:
                dp[c] = 1

        dp = sorted(dp.items(), key=lambda x: x[1], reverse=True)
        total = 0
        for idx, val in enumerate(dp):
            total += counts[idx] * val[1]

        print(total)
    except Exception as e:
        break
