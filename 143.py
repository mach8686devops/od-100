# 相同子串
while 1:
    try:
        t = input()
        p = input()
        if p in t:
            _ = t.split(p)
            print(len(_[0])+1)
        else:
            print("No")
    except Exception as e:
        break
