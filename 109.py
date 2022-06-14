# 滑动窗口和最大值

while 1:
    try:
        _ = input()
        nums = list(map(int, input().split()))
        w = int(input())

        dp = []
        for i in range(0, len(nums)-w+1):
            dp.append(sum(nums[i: i+w]))

        print(max(dp))
    except Exception as e:
        break
