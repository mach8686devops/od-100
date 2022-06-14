# 拼接url

while 1:
    try:
        sto = input()
        st = sto.split()
        a = ""
        b = ""
        if len(st) == 1:
            # 判断是 前缀还是后缀
            if sto.startswith(" "):
                b = st[0]
            else:
                a = st[0]
        elif len(st) == 2:
            a = st[0]
            b = st[1]
        else:
            print("/")
            continue

        # 我们要求 前缀不由 / 结尾
        # 结尾有多个 /
        while a.endswith("/"):
            a = a[:-1]

        # 开头有多个 /
        while b.startswith("/"):
            b = b[1:]

        # 我们要求 后缀由 / 开始
        b = f"/{b}"

        print(a+b)
    except Exception as e:
        break
