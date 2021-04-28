import random

# 隨機產生10個 [1:100]的數
nums = []
for i in range(10):
    nums.append(int(random.random() * 99 + 1))

# 使用內建排序
nums.sort()

print(nums)

# 歷變搜尋
target = int(input('Enter the target'))
include = False

for i in range(len(nums)):
    if (nums[i] == target):
        print(i)
        include = True
        break
if not include:
    print(-1)


target = int(input('Enter the target'))
include = False
index = 0

while index < len(nums):
    if (nums[index] == target):
        include = True
        print(index)
        break
    index += 1
if not include:
    print(-1)

# 二元搜尋
target = int(input('Enter the target'))
include = False
left = 0
right = len(nums) - 1
while right >= left:
    mid = int(left + (right - left) / 2)
    if (nums[mid] == target):
        print(mid)
        include = True
        break
    else :
        if target > nums[mid]:
            left = mid + 1
        else :
            right = mid - 1

if not include:
    print(-1)



