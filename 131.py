# 数组二叉树
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


while 1:
    try:
        nums = list(map(int, input().split()))

        # 构造二叉树
        root = Node(nums[0])
        stack = [root]
        i = 1
        while i < len(nums):
            r = stack[0]
            stack = stack[1:]

            r.left = Node(nums[i])
            stack.append(r.left)
            if i+1 < len(nums):
                r.right = Node(nums[i+1])
                stack.append(r.right)

            i += 2

        # 遍历数，获取路径
        dp = []

        def dfs(r, datas):
            if not r or r.data == -1:
                dp.append(datas)
                return

            dfs(r.left, datas+[r.data])
            dfs(r.right, datas+[r.data])

        dfs(root, [])
        # 根据叶子节点从小到大排序
        dp = sorted(dp, key=lambda x: x[-1])

        print(" ".join(map(str, dp[0])))
    except Exception as e:
        break
