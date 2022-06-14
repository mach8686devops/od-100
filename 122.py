# 最多字符和次数

while 1:
    try:
        nums = list(map(int, list(input())))

        dp = [0] * 10
        for n in nums:
            dp[n] += 1

        max_ = max(dp)
        print(f"{dp.index(max_)},{max_}")
    except Exception as e:
        break
