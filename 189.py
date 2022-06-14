# 水仙花数【2022 Q1 Q2 | 100分】

def fun(num):
    a, b, c = list(map(int, list(str(num))))
    return a**3 + b**3 + c**3 == num


while 1:
    try:
        base = input()
        nums = [ord(c) for c in base]

        i = 0
        j = 1

        dp = []

        def dfs(inums, subs):
            print(inums)
            i = 0
            j = 1
            while j <= len(inums):
                total = sum(inums[i: j])
                if total < 100:
                    j += 1
                elif total < 1000:
                    if fun(total):
                        dfs(inums[j:], subs+["".join([chr(n) for n in inums[i: j]])])
                    j += 1
                else:
                    break
            else:
                if "".join(subs) == base:
                    dp.append(subs)

        dfs(nums, [])

        if not dp:
            print(0)
        elif len(dp) == 1:
            print(len(dp[0]))
        else:
            print(-1)
    except Exception as e:
        break
