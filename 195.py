# 元音字母请大写
bct = "aeiou"

while 1:
    try:
        s = input()

        dp = list(s)
        for i, c in enumerate(s):
            if c in bct:
                dp[i] = c.upper()
            else:
                dp[i] = c.lower()

        print("".join(dp))
    except Exception as e:
        break
