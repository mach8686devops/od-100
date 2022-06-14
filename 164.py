# 分糖果
def dfs(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n % 2:
        # 取出、放回 + 平均分配 共两次
        return min((dfs((n - 1) / 2) + 2, dfs((n + 1) / 2) + 2))
    else:
        # 平均分配均记一次
        return dfs(n / 2) + 1


while 1:
    try:
        m = int(input())
        print(dfs(m))
    except Exception as e:
        break
