# 单词接龙
while 1:
    try:
        k = int(input())
        n = int(input())

        nums = [input() for _ in range(n)]

        # 接龙结果
        dp = [nums.pop(k)]

        while len(nums):
            # 备选单词
            cache = []
            for w in nums:
                # 上一个单词的尾字符 == 当前单词的首字符
                if dp[-1][-1] == w[0]:
                    cache.append(w)
            if cache:
                cache = sorted(cache, key=lambda x: (-len(x), x))
                next_ = cache[0]
                nums.remove(next_)
                dp.append(next_)
            else:
                break

        print("".join(dp))
    except Exception as e:
        break
