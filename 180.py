# 字符串简单数据解压缩
while 1:
    try:
        nums = input()

        lens = len(nums)
        dp = []
        key = ""
        i = 0
        j = 1
        # 拆分字符串
        while j < lens:
            if "a" <= nums[i:j] <= "z" or "A" <= nums[i:j] <= "Z":
                key += nums[i:j]
                i += 1
                j += 1
            else:
                if nums[i:j].isdigit():
                    j += 1
                else:
                    dp.append((key, int(nums[i:j-1])))
                    key = nums[j-1:j]
                    i = j
                    j += 1
        else:
            if nums[i:j].isdigit():
                dp.append((key, int(nums[i:])))
            else:
                dp.append((key+nums[i:j], 1))

        # 排序
        dp = sorted(dp, key=lambda x: x[1])

        print("".join([key*count for key, count in dp]))
    except Exception as e:
        break

# a11b2bac3bad3abcd2
# bbabcdabcdbacbacbacbadbadbadaaaaaaaaaaa

