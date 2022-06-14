# 组最大
while 1:
    try:
        nums = input().split()

        base = list(range(len(nums)))

        def dfs(val):
            if len(val) == len(nums):
                return int("".join([nums[v] for v in val]))

            for i in base:
                if i not in val:
                    return dfs(val + [i])

        dp = []
        for i in base:
            dp.append(dfs([i]))

        print(max(dp))
    except Exception as e:
        break
