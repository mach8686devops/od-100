# 连续字母
while 1:
    try:
        nums = input()

        dp = [1]
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                dp[-1] += 1
            else:
                dp.append(1)

        print(max(dp))
    except Exception as e:
        break
