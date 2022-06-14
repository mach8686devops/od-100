# 句子单词首字母大写

while 1:
    try:
        nums = input().split()

        dp = [f"{w[0].upper()}{w[1:]}" for w in nums]

        print(" ".join(dp))
    except Exception as e:
        break
