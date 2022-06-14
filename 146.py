# 括号匹配
while 1:
    try:
        nums = input()

        stack = []
        count = 0
        for c in nums:
            if c == "(":
                stack.append(c)
            elif c == ")":
                if stack and stack.pop() == "(":
                    count += 1
                else:
                    count = -1
                    break
        if stack:
            count = -1

        print(count)
    except Exception as e:
        break
