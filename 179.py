# 股票最大收益
def to_rmb(n):
    if n[-1] == "Y":
        return int(n[:-1])
    else:
        return int(n[:-1])*7


while 1:
    try:
        prices = list(map(to_rmb, input().split()))

        if not prices:
            print(0)
            break

        maxpro = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maxpro += prices[i] - prices[i - 1]
        print(maxpro)
    except Exception as e:
        break
