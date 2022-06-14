# 数大雁
while 1:
    try:
        chars = input()

        dp = []

        def dfs(nums):
            # 确定一个有效的叫声范围
            s = 0
            e = 0
            for c in "uack":
                e += nums[e:].index(c)
            e += 1

            dct = {
                "q": 0,
                "u": 0,
                "a": 0,
                "c": 0,
                "k": 0,
            }
            k = 0
            while k < len(nums):
                if nums[k] == "q":
                    if s <= k <= e:
                        dct["q"] += 1
                else:
                    dct[nums[k]] += 1
                k += 1

            # 如果其他字母计数小于
            dp.append(min(dct.values()))

        i = 0
        while "q" in chars[i:]:
            i = chars.index("q")
            dfs(chars[i:])
            chars = chars[i+1:]

        print(max(dp))
    except Exception as e:
        break
