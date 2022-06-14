# 圆桌队列
while 1:
    try:
        n = int(input())
        k = int(input())
        m = int(input())

        nums = list(range(1, n+1))
        nums = nums[k-1:] + nums[:k-1]
        dp = []

        while len(nums) >= m:
            cache = list(range(m - 1, len(nums), m))
            nums_ = []
            for i in range(len(nums)):
                if i in cache:
                    dp.append(nums[i])
                elif i > cache[-1]:
                    nums = nums[i:] + nums_
                    break
                else:
                    nums_.append(nums[i])
            else:
                nums = nums_

        print(dp[-1])
    except Exception as e:
        break
