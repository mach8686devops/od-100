while 1:
    try:
        import sys

        n, k = [int(i) for i in input().replace("\n", "").split()]
        ans = 0
        line = sys.stdin.readline().strip()
        nums = list(map(int, line.split()))

        for i in range(1, n):
            if nums[i] > nums[i - 1] * k or nums[i] < nums[i - 1] / k:
                ans += 1
        print(ans)
    except Exception as e:
        print(e)
        pass
