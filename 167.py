# 找出字符串中最小和最大数字

while 1:
    try:
        nums = list(map(int, input().split(",")))
        print(len(nums) - nums.count(min(nums)) - nums.count(max(nums)))
    except Exception as e:
        break
