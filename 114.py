# 书籍叠放

while 1:
    try:
        n = int(input())

        nums = [list(map(int, input().split())) for _ in range(n)]

        dp = []
        lens = len(nums)

        def dfs(sub, count=1):
            if count >= lens:
                dp.append(len(sub))
            else:
                for i in range(lens):
                    if i not in sub:
                        if nums[i][0] < nums[sub[-1]][0] and nums[i][1] < nums[sub[-1]][1]:
                            dfs(sub+[i], count+1)

        for i in range(lens):
            dfs([i])

        print(max(dp))
    except Exception as e:
        break
