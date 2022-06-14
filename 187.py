# 二叉树中序
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_node(c):
    if type(c) == Node:
        return c
    elif c:
        return Node(c)
    else:
        return None


def get_root(stack):
    j = len(stack) - 1
    while j >= 0:
        if stack[j] == "{":
            break
        j -= 1

    if stack[j:][1] == ",":
        left_ = None
    else:
        left_ = get_node(stack[j:][1])

    if stack[j:][-1] == "," or "," not in stack[j:]:
        right_ = None
    else:
        right_ = get_node(stack[j:][-1])

    stack = stack[:j]
    root_ = get_node(stack.pop(-1))
    root_.left = left_
    root_.right = right_
    stack.append(root_)
    return stack


while 1:
    try:
        chars = input().replace(" ", "")

        # 构建树
        stack = []
        for c in chars:
            if c == "}":
                stack = get_root(stack)
            else:
                stack.append(c)

        dp = []

        # 中序输出
        def dfs(root):
            if not root:
                return

            dfs(root.left)
            dp.append(root.val)
            dfs(root.right)

        dfs(stack[0])
        print("".join(dp))
    except Exception as e:
        break
