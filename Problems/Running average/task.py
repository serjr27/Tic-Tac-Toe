nums = [int(i) for i in input().strip()]
print([(nums[i] + nums[i + 1]) / 2 for i in range(len(nums) - 1)])
