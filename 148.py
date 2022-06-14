# 倒序输出

while 1:
    try:
        nums = input()

        flg = ""
        if nums[0] == "-":
            flg = "-"
            nums = nums[1:]

        ret = ""
        for c in nums[::-1]:
            if c not in ret:
                ret += c

        print(f"{flg}{int(ret)}")
    except Exception as e:
        break
