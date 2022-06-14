# 停车位问题【2022 Q2 | 100分】

while 1:
    try:
        nums = input().split()

        max_ = 0
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j] == "0":
                j += 1
            else:
                max_ = max([max_, j - i])
                i = j
                j = j + 1

        # 减去一个当前车的位置
        print(max_ - 1)
    except Exception as e:
        break
