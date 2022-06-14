# 考古学家【2022 Q2 | 100分】
while 1:
    try:
        chars = input().split()

        dp = []

        # 对碎片进行组合
        def dfs(sub):
            if len(sub) == len(chars):
                t = "".join(sub)
                # 剔除重复的结果
                # 比如 abab 可以是 a + b + ab  或 ab + a + b
                if t not in dp:
                    dp.append(t)
            else:
                for c in chars:
                    # 剔除重复的碎片
                    if c not in sub:
                        dfs(sub + [c])

        for c in chars:
            dfs([c])

        print(" ".join(dp))
    except Exception as e:
        break

