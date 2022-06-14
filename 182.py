# 字符串分割
while 1:
    try:
        k = int(input())
        head, tail = input().split("-", 1)

        tail = tail.replace("-", "")
        temp = ""
        for index in range(0, len(tail), k):
            line = tail[index: index + k]
            count1 = 0
            count2 = 0
            for c in line:
                if "A" <= c <= "Z":
                    count1 += 1
                if "a" <= c <= "z":
                    count2 += 1
            if count1 == count2:
                temp += line
            elif count1 > count2:
                temp += line.upper()
            else:
                temp += line.lower()

            # 按长度k分隔处理后的字符串
        dp = []
        for index in range(0, len(temp), k):
            dp.append(temp[index: index + k])

        print(f"{head}-{'-'.join(dp)}")

        # 推导式写法
        # print(f"{head}-{'-'.join([temp[index: index+k] for index in range(0, len(temp), k)])}")
    except Exception as e:
        break
