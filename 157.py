# 相加

while 1:
    try:
        a, n = input().split()

        total = 0
        for i in range(1, int(n) + 1):
            total += int(a * i)

        print(total)
    except Exception as e:
        break
