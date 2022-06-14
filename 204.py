# 分苹果
# 二进制的加法 不计算走位

while 1:
    try:
        n = int(input())
        nums = list(map(int, input().split()))
        max_ = sum(nums)

        dp = []

        def get_w(sub):
            t = 0
            for n in set(nums).difference(sub):
                # 按照二进制加法计算
                t = t ^ n
            return t

        def dfs(w, sub):
            if w == get_w(sub):
                tot = sum(sub)
                dp.append(max(tot, max_ - tot))
                return
            elif len(sub) == len(nums) - 1:
                return
            else:
                for wi in nums:
                    if wi not in sub:
                        dfs(w ^ wi, sub.union({wi}))

        for w in nums:
            dfs(w, {w})

        if dp:
            print(max(dp))
        else:
            print(-1)
    except Exception as e:
        break
