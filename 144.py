# 矩形面积
while 1:
    try:
        xs = []
        ys = []

        coms_d = []
        coms_e = []
        for _ in range(int(input())):
            l = input().split()
            x1, y1, x2, y2 = list(map(int, l[1:]))
            xs.append(x1)
            xs.append(x2)
            ys.append(y1)
            ys.append(y2)
            if l[0] == 'd':
                coms_d.append((x1, y1, x2, y2))
            else:
                coms_e.append((x1, y1, x2, y2))

        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)

        # 坐标轴偏移量
        x = 0 - min_x
        y = 0 - min_y
        dp = [[0] * abs(max_y-min_y) for _ in range(abs(max_x-min_x))]

        for x1, y1, x2, y2 in coms_d:
            # 需要 转成 二维数组的下标
            for i in range(min((x2, x1)) + x, max((x2, x1)) + x):
                for j in range(min((y2, y1)) + y, max((y2, y1)) + y):
                    dp[i][j] = 1
        for x1, y1, x2, y2 in coms_e:
            for i in range(min((x2, x1)) + x, max((x2, x1)) + x):
                for j in range(min((y2, y1)) + y, max((y2, y1)) + y):
                    dp[i][j] = 0

        print(sum([sum(i) for i in dp]))
    except Exception as e:
        break
