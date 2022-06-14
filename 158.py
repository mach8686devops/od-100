# 水果搬运


while 1:
    try:
        _ = input()
        nums = []
        while 1:
            try:
                m, p, q = input().split()
                nums.append((m, int(p), int(q)))
            except:
                break

        nums = sorted(nums, key=lambda x: (x[0], x[2], x[1]))
        for i in nums:
            print(" ".join(list(map(str, i))))
    except Exception as e:
        break
