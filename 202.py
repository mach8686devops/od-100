# 翻转单词

while 1:
    try:
        s = input().split()
        n, m = list(map(int, input().split()))
        if n >= m:
            print(s)
        else:
            if n < 0:
                n = 0
            if m > len(s):
                m = len(s) - 1

            s0 = s[:n]
            s1 = s[n:m+1]
            s2 = s[m+1:]
            print(" ".join(s0 + s1[::-1] + s2))
    except Exception as e:
        break
