# 数字分解

while 1:
    try:
        num = int(input())

        dp = [[num]]


        def dfs(n):
            total = sum(n)
            if total == num:
                dp.append(n)
            elif total > num:
                return
            else:
                dfs(n + [n[-1] + 1])


        for i in range(1, (num // 2 + 1)):
            dfs([i])

        print(len(dp))
    except Exception as e:
        break
