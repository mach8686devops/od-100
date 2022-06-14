# 输出匹配字符串的开始下标
while 1:
    try:
        a = input()
        b = input()
        if b in a:
            print(a.index(b))
        else:
            print(-1)
    except Exception as e:
        break
