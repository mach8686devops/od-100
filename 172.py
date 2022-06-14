# 敏感字段加密
while 1:
    try:
        k = int(input())

        nums = input()

        dp = []

        temp = ""
        for c in nums:
            if c == "_":
                if '"' not in temp and temp:
                    dp.append(temp)
                    temp = ""
                elif '"' in temp:
                    temp += c
            elif c == '"':
                if temp and '"' in temp:
                    temp += c
                    dp.append(temp)
                    temp = ""
                elif temp and '"' not in temp:
                    dp.append(temp)
                    temp = c
                elif not temp:
                    temp = c
            else:
                temp += c
        if temp:
            dp.append(temp)

        dp[k] = "*"*6
        print("_".join(dp))
    except Exception as e:
        break
