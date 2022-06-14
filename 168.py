# 成绩及格线

while 1:
    try:
        nums = map(int, input().split())
        nums = sorted(nums, reverse=True)

        # 60% 的及格线
        base = nums[5] // 10 * 10
        if base > 60:
            print(60)
        else:
            print(base)

    except Exception as e:
        break

# 90 78 61 28 54 46 92 98 49 50
# 50
