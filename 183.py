# 长廊电灯数
while 1:
    try:
        n = int(input())
        base = [False] * (n+1)

        for i in range(1, n+1):
            for j in range(1, n+1):
                index = j*i
                if index > n:
                    break
                else:
                    base[index] = not base[index]
        print(sum(base))

    except Exception as e:
        break
