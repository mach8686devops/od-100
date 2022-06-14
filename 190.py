# IPv4地址转换成整数【2022 Q2|100】
while 1:
    try:
        nums = list(map(int, input().split("#")))
        if len(nums) != 4:
            print("invalid IP")
        else:
            dp = ""
            for i in range(4):
                if not ((i == 0 and 1 <= nums[i] <= 128) or (i > 0 and 0 <= nums[i] <= 255)):
                    print("invalid IP")
                    break

                dp += bin(nums[i])[2:].zfill(8)
            else:
                print(int(dp, 2))
    except Exception as e:
        break
