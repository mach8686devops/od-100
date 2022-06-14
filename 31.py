while 1:
    try:
        s = input().strip()
        target = input().strip()
        ret = s.find(target)
        if ret > 0:
            print(ret+1)
        else:
            print("No")
    except Exception as e:
        break

