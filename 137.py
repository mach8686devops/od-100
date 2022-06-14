# 喊7
while 1:
    try:
        nums = list(map(int, input().split()))

        lens = len(nums)
        max_ = max(nums)

        dp = [0] * lens
        i = 1
        while max(dp) < max_:
            if i % 7 == 0 or "7" in str(i):
                dp[(i % lens) - 1] += 1
            i += 1

        print(dp)
    except Exception as e:
        break
