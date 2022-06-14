# 求数组的最小数和最大数之和

while 1:
    try:
        nums = list(map(int, input().split(",")))
        print(min(nums) + max(nums))
    except Exception as e:
        break
