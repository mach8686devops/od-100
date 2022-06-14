# 有N个正整数组成的一个序列
# 给定一个整数sum
# 求长度最长的的连续子序列使他们的和等于sum
# 返回次子序列的长度
# 如果没有满足要求的序列 返回-1
# 案例1：
# 输入
# 1,2,3,4,2
# 6
# 输出
# 3
# 解析：1,2,3和4,2两个序列均能满足要求
# 所以最长的连续序列为1,2,3 因此结果为3


# 1,2,3,4,2
# 6
# 3

while 1:
    try:
        import sys

        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        arrays = list(map(int, line.split(",")))
        target = int(input())
        n = len(arrays)
        left = 0
        right = 1
        ret = 0
        while right < n:
            val = sum(arrays[left:right])
            if val == target:
                ret = max(ret, right - left)
                left += 1
                right += 1
            elif val > target and left < right:
                left += 1
            elif val > target:
                right += 1
            else:
                right += 1
        print(ret if ret else -1)
    except Exception as e:
        break
