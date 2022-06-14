# 电话号码的翻译
dct = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "double": "#",
}

while 1:
    try:
        nums = input()

        for k, v in dct.items():
            nums = nums.replace(k, v)

        ret = []
        i = 0
        while i < len(nums):
            if "0" <= nums[i] <= "9":
                ret.append(nums[i])
            elif nums[i] == "#":
                if i + 1 < len(nums) and "0" <= nums[i+1] <= "9":
                    ret.append(nums[i+1])
                else:
                    print("error")
                    break
            else:
                print("error")
                break
            i += 1
        else:
            print("".join(ret))
    except Exception as e:
        break
