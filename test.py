while 1:
    try:
        import sys
        n = int(input().strip())
        ans = []
        s = sys.stdin.readline().strip()
        while s != "":
            vals = s.split(" ")
            for val in vals:
                ans.append(int(val))
            s = sys.stdin.readline().strip("\n")
        from collections import Counter

        d = dict(Counter(ans))
        ant = []
        ans = list(d.values())
        for x, y in d.items():
            if y == max(ans):
                ant.append(x)

        m = len(ant)
        # 三个的情况
        if m % 2 == 1 and m >= 3:
            print(ant[(m - 1) // 2])
        elif m == 1:
            print(ant[0])
        else:
            print(ant)

    except Exception as e:
        break

# 1 2
# 2 3
# 3 4
# 4 5
