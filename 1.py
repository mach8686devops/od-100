# 寻找身高相近的小朋友
# sorted key的使用

while 1:
    try:
        H, m = map(int, input().split())
        nums = list(map(int, input().split()))

        nums = sorted(nums, key=lambda x: (abs(x - H), x))
        print(" ".join(map(str, nums)))
    except Exception as e:
        break

# 100 11
# 95 96 97 98 99 102 103 104 105 106 108
# 99 98 102 97 103 96 104 95 105 106 108
