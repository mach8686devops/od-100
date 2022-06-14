# 跳格子
while 1:
    try:
        n = int(input())

        nums = []
        for _ in range(n):
            x = input().split()
            if x and len(x) == 2:
                nums.append(tuple(map(int, x)))
            else:
                break

        nums = sorted(nums, key=lambda x: x[0])

        # 格子开启状态表
        state = [1] * n
        for start, end in nums:
            state[end] = 0

        # 没有起始的格子
        if max(state) == 0:
            print("no")
            continue

        dp = [0]

        def dfs(s, link):
            # 所有节点都已开启
            if len(link) == len(nums) and sorted(link, key=lambda x: x[0]) == nums:
                dp.append(1)
                return

            ends = []
            for start_, end_ in nums:
                if s == start_:
                    link.append((start_, end_))
                    ends.append(end_)

            for end_ in ends:
                dfs(end_, link)

        # 从状态开启的节点，进行递归
        for i in range(n):
            if state[i] == 1:
                dfs(i, [])

        if max(dp):
            print("yes")
        else:
            print("no")

    except Exception as e:
        break
