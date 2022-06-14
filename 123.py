# 约瑟夫问题

while 1:
    try:
        nums = list(map(int, input().split(",")))
        m = int(input())

        dp = []
        i = 0
        c = 1
        while nums:
            if i == len(nums):
                i = 0

            if c % m == 0:
                m = nums.pop(i)
                dp.append(m)
                c = 1
            else:
                i += 1
                c += 1

        print(",".join(map(str, dp)))
    except Exception as e:
        break
