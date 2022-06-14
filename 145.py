# 括号的匹配二
while 1:
    try:
        nums = input()

        stack = []
        flg = True
        for c in nums:
            if c in "([{":
                stack.append(c)
            elif c in ")]}":
                if stack:
                    w = stack.pop()
                    if not ((c == ")" and w == "(")
                            or (c == "]" and w == "[")
                            or (c == "}" and w == "{")):
                        flg = False
                        break
                else:
                    flg = False
                    break
        if stack:
            flg = False

        print("true" if flg else "false")
    except Exception as e:
        break
