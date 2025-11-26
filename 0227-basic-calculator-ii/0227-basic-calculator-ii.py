class Solution(object):
    def calculate(self, s):
        s = s.replace(" ", "") 

        nums = []
        ops = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                nums.append(num)
                continue
            else:
                ops.append(s[i])
            i += 1

        # print("nums:" ,nums)

        i = 0
        while i < len(ops):
            if ops[i] == "*":
                nums[i] = nums[i] * nums[i+1]
                nums.pop(i+1)
                ops.pop(i)
            elif ops[i] == "/":
                nums[i] = int(nums[i] / nums[i+1])
                nums.pop(i+1)
                ops.pop(i)
            else:
                i += 1

        i = 0
        while i < len(ops):
            if ops[i] == "+":
                nums[i] = nums[i] + nums[i+1]
                nums.pop(i+1)
                ops.pop(i)
            elif ops[i] == "-":
                nums[i] = nums[i] - nums[i+1]
                nums.pop(i+1)
                ops.pop(i)
            else:
                i += 1

        return nums[0]
