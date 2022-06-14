# 字符串以 N 为单位分段
while 1:
    try:
        m, n = list(map(int, input().split()))
        nums = input().split()

        for c in nums:
            print(",".join([c[i: i+n].ljust(n, "0") for i in range(0, len(c), n)]))

    except Exception as e:
        break
