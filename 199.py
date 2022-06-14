# 全排列2
while 1:
    try:
        nums = list(map(int, input().split(",")))

        base = [i for i in range(len(nums))]
        base_dp = []

        def dfs(s):
            if len(s) == len(nums):
                base_dp.append(s)
            else:
                for c in base:
                    if c not in s:
                        dfs(s + [c])

        for c in base:
            dfs([c])

        dp = []
        for i in base_dp:
            temp = [nums[j] for j in i]
            if temp not in dp:
                dp.append(temp)

        print(dp)
    except Exception as e:
        break
