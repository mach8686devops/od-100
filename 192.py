# 整数翻转
while 1:
    try:
        num = input()
        # 超出长度 返回0
        if len(num) > 32:
            print("0")
        else:
            # 有符号 除第一位进行反转
            if num[0] in "+-":
                print(num[0] + num[1:][::-1])
            else:
                print(num[::-1])
    except Exception as e:
        break
