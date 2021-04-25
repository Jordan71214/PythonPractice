import random
nums = []
for i in range(10):
    nums.append(int(random.random() * 99 + 1))
print(nums)

# 氣泡排序
for i in range(len(nums) - 1):
    for j in range(len(nums) - i - 1):
        if nums[j] > nums[j + 1]:
            temp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = temp

print(nums)