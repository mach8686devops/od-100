# 兔子繁殖
while 1:
    try:
        month = int(input())
        dp = [1]


        def dfs(n, h):
            if h > month:
                return

            if n > 3:
                dp.append(1)
                dfs(2, h + 1)

            dfs(n + 1, h + 1)

        dfs(1, 1)
        print(sum(dp))
    except Exception as e:
        break
