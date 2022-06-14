# 特殊计算
while 1:
    try:
        nums = input()

        stack = []
        i = 0
        j = 1
        while j < len(nums):
            if nums[j] == "#":
                stack.append(int("".join(nums[i:j])))
                stack.append(nums[j])
                i = j + 1
            elif nums[j] == "$":
                stack.append(int("".join(nums[i:j])))
                stack.append(nums[j])
                i = j + 1
            j += 1
        else:
            stack.append(int("".join(nums[i:j])))

        while "#" in stack:
            i = stack.index("#")
            stack[i-1] = 2 * stack[i-1]
            stack.pop(i)

        while "$" in stack:
            i = stack.index("$")
            stack[i+1] = 3 * stack[i+1]
            stack.pop(i)

        print(sum(stack))
    except Exception as e:
        break
