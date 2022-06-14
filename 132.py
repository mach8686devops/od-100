# 素数
dp = {}

def func(n):
    # 判断是否是素数
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    for i in range(3, n, 2):
        if n % i == 0:
            return False
    dp[n] = True
    return True


while 1:
    try:
        num = int(input())

        for i in range(2, num//2):
            c = num // i
            if c >= i and c*i == num and func(c) and func(i):
                print(f"{i} {c}")
                break
        else:
            print(-1)
    except Exception as e:
        break
