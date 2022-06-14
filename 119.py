# 面试官数量

while 1:
    try:
        n = int(input())

        nums = []
        for _ in range(n):
            nums.append(list(map(int, input().split())))

        nums = sorted(nums, key=lambda x: x[0])
        max_ = max([e for s, e in nums])

        dp = [0] * (max_+1)

        for s, e in nums:
            for i in range(s, e+1):
                dp[i] += 1

        print(max(dp))
    except Exception as e:
        break
