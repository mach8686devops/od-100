# 补种胡杨
while 1:
    try:
        n = int(input())
        m = int(input())
        nums = list(map(int, input().split()))
        k = int(input())

        nums = [0 if i + 1 in nums else 1 for i in range(n)]

        max_ = 0
        i = 0
        j = min(k, n)
        while j < len(nums):
            count = nums[i:j].count(0)
            if count < k:
                j += 1
            elif count == k:
                max_ = max([j-i, max_])
                j += 1
            else:
                i += 1
        else:
            max_ = max([j - i, max_])

        print(max_)
    except Exception as e:
        break
