# 数组中不同的一个数

while 1:
    try:
        nums = list(map(int,input().split()))
        # ret = 0
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        print(nums[0])
    except Exception as e:
        break

