# 相同字符的字符串
while 1:
    try:
        nums = input().split()
        key = input()

        dp = []
        for word in nums:
            if key in word:
                dp.append(word)

        print(" ".join(dp))
    except Exception as e:
        break
