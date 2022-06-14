while 1:
    try:
        nums = input()

        flg = "RIGTH"
        stack = []
        for c in nums:
            if c == "(":
                stack.append(c)
            elif c == ")":
                if not stack or stack.pop() != "(":
                    flg = "WRONG"
                    break
        if stack:
            flg = "WRONG"

        print(f"{flg} {nums.count('(')} {nums.count(')')}")
    except Exception as e:
        break
