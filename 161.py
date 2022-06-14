# 跳跃比赛
def dfs(nums, i=0):
    if len(nums) <= i+1:
        return 0

    return min([dfs(nums, i+j)+1 for j in range(1, nums[i]+1)])


while 1:
    try:
        _ = input()

        nums = list(map(int, input().split()))

        print(dfs(nums))
    except Exception as e:
        break
