# 密钥格式化
while 1:
    try:
        # 分割第一的 - 前后的字符串 位 s1 s2
        s1, s2 = input().split("-", 1)
        k = int(input())

        # s2 需要去除分隔符，转大写
        # 按长度 k 重新分隔
        s2 = s2.replace("-", "").upper()

        dp = []
        for i in range(0, len(s2), k):
            dp.append(s2[i: i + k])

        s2 = "-".join(dp)
        print(f"{s1}-{s2}")
    except Exception as e:
        break
