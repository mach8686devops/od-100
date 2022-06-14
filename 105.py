# 员工工号
while 1:
    try:
        max_, y = list(map(int, input().split()))

        z = 26**y
        for i in range(1, 9-y):
            if z * (10**i) >= max_:
                print(i)
                break

    except Exception as e:
        break
